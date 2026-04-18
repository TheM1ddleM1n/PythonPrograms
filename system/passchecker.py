import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import re
import math
import hashlib
import requests

password_history = set()


def add_to_history(password):
    h = hashlib.sha256(password.encode("utf-8")).hexdigest()
    password_history.add(h)


def in_history(password):
    h = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return h in password_history


def password_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)


def crack_time(entropy_bits):
    guesses_per_second = 1e12
    seconds = 2**entropy_bits / guesses_per_second

    if seconds < 1:
        return "Instantly"
    if seconds < 60:
        return "Seconds"
    if seconds < 3600:
        return "Minutes"
    if seconds < 86400:
        return "Hours"
    if seconds < 86400 * 30:
        return "Days"
    if seconds < 86400 * 365:
        return "Months"
    return "Years"


def is_pwned(password):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        res = requests.get(url, timeout=5)
        for line in res.text.splitlines():
            h, count = line.split(":")
            if h == suffix:
                return True
        return False
    except Exception:
        return False


def update_meter(score):
    meter["value"] = score

    if score <= 2:
        meter_label.config(text="Weak", foreground="#ff4444")
    elif score <= 4:
        meter_label.config(text="Medium", foreground="#ffaa00")
    else:
        meter_label.config(text="Strong", foreground="#44ff44")


def check_strength():
    password = entry_password.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    if in_history(password):
        messagebox.showwarning("Warning", "You have used this password before.")
        return

    score = 0
    missing = []

    if len(password) >= 8:
        score += 1
    else:
        missing.append("at least 8 characters")

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        missing.append("an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        missing.append("a lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        missing.append("a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        missing.append("a special character")

    update_meter(score)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    entropy_bits = password_entropy(password)
    crack = crack_time(entropy_bits)
    pwned = is_pwned(password)

    result = ""
    result += "Password Strength Check\n"
    result += "------------------------\n"
    result += f"Strength: {strength}\n"
    result += f"Entropy: {entropy_bits:.2f} bits\n"
    result += f"Estimated Crack Time: {crack}\n"
    result += f"Breach Status: {'⚠️ Found in breaches!' if pwned else 'Not found'}\n"

    if missing:
        result += "\nSuggestions:\n"
        for item in missing:
            result += f" • Add {item}\n"

    text_output.config(state="normal")
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)
    text_output.config(state="disabled")

    if strength == "Strong" and not pwned:
        add_to_history(password)


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(chars) for _ in range(16))

    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

    update_meter(0)

    text_output.config(state="normal")
    text_output.delete("1.0", tk.END)
    text_output.config(state="disabled")


def toggle_password():
    if entry_password.cget("show") == "":
        entry_password.config(show="•")
        btn_toggle.config(text="Show")
    else:
        entry_password.config(show="")
        btn_toggle.config(text="Hide")


root = tk.Tk()
root.title("Password Tool")
root.geometry("500x520")
root.resizable(False, False)
root.configure(bg="#000000")

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TLabel", background="#000000", foreground="#00ff00", font=("Consolas", 11)
)
style.configure(
    "TButton", background="#003300", foreground="#00ff00", font=("Consolas", 11)
)
style.map("TButton", background=[("active", "#005500")])

label = ttk.Label(root, text="Enter Password:")
label.pack(pady=10)

frame = ttk.Frame(root)
frame.pack()

entry_password = ttk.Entry(frame, width=30, show="•", font=("Consolas", 12))
entry_password.pack(side="left", padx=5)

btn_toggle = ttk.Button(frame, text="Show", width=6, command=toggle_password)
btn_toggle.pack(side="left")

btn_check = ttk.Button(root, text="Check Strength", command=check_strength)
btn_check.pack(pady=10)

btn_generate = ttk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack()

meter_label = ttk.Label(root, text="Strength:")
meter_label.pack(pady=5)

meter = ttk.Progressbar(root, length=300, maximum=6)
meter.pack(pady=5)

text_output = tk.Text(
    root,
    height=12,
    width=60,
    state="disabled",
    bg="#001100",
    fg="#00ff00",
    font=("Consolas", 11),
)
text_output.pack(pady=10)

root.mainloop()
