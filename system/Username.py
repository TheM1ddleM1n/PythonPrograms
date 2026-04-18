import re

print("Username Generator\n" + "-" * 20)

try:
    # Get and clean input
    first = input("First name: ").strip().lower()
    last = input("Surname: ").strip().lower()
    year = input("Year of birth (YYYY): ").strip()

    # Regex validation: Names must be letters/spaces/hyphens; The year must be 4 digits
    if not (
        re.fullmatch(r"[a-z\s\-']+", first)
        and re.fullmatch(r"[a-z\s\-']+", last)
        and re.fullmatch(r"\d{4}", year)
    ):
        raise ValueError("Invalid format. Use letters for names and 4 digits for year.")

    username = f"{last[:4]}{first[0]}{year[1:]}"

    print(f"\nYour username: {username}")

except ValueError as e:
    print(f"Error: {e}")
