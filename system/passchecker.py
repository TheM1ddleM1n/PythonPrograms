import re

common_passwords = ["password", "123456", "qwerty", "abc123"]

print("Password Strength Checker")
print("-" * 25)

while True:
    password = input("\nEnter a password: ")

    score = 0
    missing = []

    # Common password check
    if password.lower() in common_passwords:
        print("❌ This password is too common!")
        continue

    # Length
    if len(password) >= 8:
        score += 1
    else:
        missing.append("at least 8 characters")

    if len(password) >= 12:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        missing.append("an uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        missing.append("a lowercase letter")

    # Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        missing.append("a number")

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        missing.append("a special character")

    # Strength rating
    print("\nResult:")

    if score <= 2:
        strength = "Weak"
        bar = "█░░░░░"
    elif score <= 4:
        strength = "Medium"
        bar = "███░░░"
    else:
        strength = "Strong"
        bar = "██████"

    print("Strength:", strength)
    print("Bar:     ", bar)

    # Show missing parts
    if missing:
        print("Improve by adding:", ", ".join(missing))

    # Stop only if strong
    if strength == "Strong":
        print("\n✅ Good password!")
        break
    else:
        print("\nTry again.")
