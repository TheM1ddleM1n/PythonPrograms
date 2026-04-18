"""Lucky number calculator based on birth details."""

print("Welcome to the Lucky program!")
try:
    month = int(input("Please enter the month number e.g. November is 11: "))
    year = int(input("Please enter the last two numbers of your year e.g. 01: "))
    day = int(
        input(
            "Please enter the first number of the day of your birthday\n for example if your birthday is on the 16th day of the month, enter 1: "
        )
    )

    lucky_number = month + year + day
    print(f"Your lucky number is {lucky_number}")

except ValueError:
    print("❌ Error: Please enter valid numbers only.")
