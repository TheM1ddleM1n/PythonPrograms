import os
import re
import random
import urllib.request
import urllib.error
from datetime import date

OWNER = "TheM1ddleM1n"
OWNER_NORMALISED = OWNER.lower()
OWNER_BIRTHDAY = (6, 5)

GITHUB_USERNAME_RE = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-]{0,37}[a-zA-Z0-9]$|^[a-zA-Z0-9]$')

BIRTHDAY_MESSAGES = [
    "Hope your day is as amazing as your code!",
    "Wishing you a bug-free birthday and smooth deployments!",
    "May your birthday be full of joy, cake, and zero stack traces!",
    "Another year wiser, another year of awesome Python programs!",
    "Here's to you — keep building great things!",
    "May your commits always be clean and your birthdays always sweet!",
    "Wishing you infinite loops of happiness today!",
    "You're not getting older, your version number is just incrementing!",
]

OWNER_BIRTHDAY_MESSAGES = [
    "The creator himself! PythonProgramsV3 wouldn't exist without you — happy birthday, TheM1ddleM1n!",
    "The mastermind behind it all turns another year older! Hope it's an epic one, TheM1ddleM1n!",
    "Happy birthday to the one who started it all! PythonProgramsV3 salutes you, TheM1ddleM1n!",
    "The legend himself! Wishing you the best birthday yet — you've earned it, TheM1ddleM1n!",
    "From every script, every commit, every contributor — happy birthday, TheM1ddleM1n!",
]

IMPERSONATOR_MESSAGES = [
    "That username belongs to the creator of PythonProgramsV3. Nice try!",
    "You're not fooling anyone — that's TheM1ddleM1n's username!",
    "Impersonating the creator? Bold move. Blocked.",
]

COUNTDOWN_MESSAGES = [
    "Keep coding until the big day arrives!",
    "Your birthday is loading... please wait!",
    "Almost there — stay bug-free until then!",
    "The countdown is on. Keep shipping great code!",
    "Not long now — save some cake for the rest of us!",
]

OWNER_COUNTDOWN_MESSAGES = [
    "The creator's birthday is coming — PythonProgramsV3 is getting ready to celebrate!",
    "Counting down to the day the legend was born!",
    "The mastermind's birthday approaches. This repo can't wait!",
]


def validate_github_username(username):
    return bool(GITHUB_USERNAME_RE.match(username))


def github_user_exists(username):
    url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "PythonProgramsV3-BirthdayChecker"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        print(f"GitHub API error: {e.code}")
        return False
    except urllib.error.URLError as e:
        print(f"Network error reaching GitHub API: {e.reason}")
        return False


def days_until_birthday(birth_month, birth_day):
    today = date.today()
    next_bday = date(today.year, birth_month, birth_day)
    if next_bday < today:
        next_bday = date(today.year + 1, birth_month, birth_day)
    return (next_bday - today).days


def verify_owner_token():
    token_input = os.environ.get("OWNER_TOKEN_INPUT", "").strip()
    token_secret = os.environ.get("OWNER_TOKEN_SECRET", "").strip()
    if not token_secret:
        return False
    return token_input == token_secret


def main():
    username = os.environ.get("BIRTHDAY_USERNAME", "").strip()
    birthday_str = os.environ.get("BIRTHDAY_DATE", "").strip()

    print("=" * 50)

    if not username:
        print("No username provided. Exiting.")
        print("=" * 50)
        return

    if not validate_github_username(username):
        print(f"'{username}' is not a valid GitHub username format.")
        print("Only letters, numbers, and hyphens are allowed (max 39 chars).")
        print("=" * 50)
        return

    is_owner_username = username.lower() == OWNER_NORMALISED

    if is_owner_username and not verify_owner_token():
        print(f"Username '{username}' requires the owner token to unlock creator mode.")
        print("Running as a standard user instead.")
        print("=" * 50)
        is_owner_username = False

    print(f"Checking GitHub for user '{username}'...")

    if not github_user_exists(username):
        print(f"No GitHub account found for '{username}'. Exiting.")
        print("=" * 50)
        return

    print(f"GitHub user '{username}' verified.")
    print("=" * 50)

    if not birthday_str:
        print("No birthday provided. Exiting.")
        print("=" * 50)
        return

    try:
        parts = birthday_str.split("-")
        if len(parts) != 2:
            raise ValueError
        birth_month = int(parts[0])
        birth_day = int(parts[1])
        if not (1 <= birth_month <= 12 and 1 <= birth_day <= 31):
            raise ValueError
    except ValueError:
        print("Invalid birthday format. Please use MM-DD (e.g. 06-05).")
        print("=" * 50)
        return

    is_owner_date_claim = (birth_month, birth_day) == OWNER_BIRTHDAY and not is_owner_username

    if is_owner_date_claim:
        print(random.choice(IMPERSONATOR_MESSAGES))
        print("=" * 50)
        return

    today = date.today()
    is_birthday = today.month == birth_month and today.day == birth_day

    print(f"Hello, {username}!")
    print("=" * 50)

    if is_birthday:
        if is_owner_username:
            message = random.choice(OWNER_BIRTHDAY_MESSAGES)
            print()
            print("  👑🎂🎉 HAPPY BIRTHDAY, CREATOR! 🎉🎂👑")
            print()
            print(f"  Happy Birthday from PythonProgramsV3, {username}!")
            print()
            print(f"  {message}")
            print()
        else:
            message = random.choice(BIRTHDAY_MESSAGES)
            print()
            print("  🎂🎉🎈 HAPPY BIRTHDAY! 🎈🎉🎂")
            print()
            print(f"  Happy Birthday from PythonProgramsV3, {username}!")
            print()
            print(f"  {message}")
            print()
    else:
        days = days_until_birthday(birth_month, birth_day)
        message = random.choice(
            OWNER_COUNTDOWN_MESSAGES if is_owner_username else COUNTDOWN_MESSAGES
        )
        print()
        if days == 1:
            print(f"  🎂 Your birthday is TOMORROW, {username}!")
        else:
            print(f"  📅 You have {days} days until your birthday, {username}!")
        print()
        print(f"  {message}")
        print()

    print("=" * 50)


if __name__ == "__main__":
    main()
