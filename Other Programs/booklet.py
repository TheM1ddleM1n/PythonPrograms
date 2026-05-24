from datetime import date
import random


def ordinal(n):
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    if n % 10 == 1:
        return f"{n}st"
    if n % 10 == 2:
        return f"{n}nd" # codespell:ignore nd
    if n % 10 == 3:
        return f"{n}rd"
    return f"{n}th"


def birthday_program():
    print("\nBirthday Program")

    name = input("What is your full name?: ").strip()
    print(f"\nNice to meet you, {name}.")

    while True:
        try:
            d = int(input("\nDay you were born (1-31): "))
            m = int(input("Month you were born (1-12): "))
            y = int(input("Year you were born (YYYY): "))

            today = date.today()
            birth = date(y, m, d)

            if birth > today:
                print("That birth date is in the future. Try again.")
                continue

            age = today.year - y - ((today.month, today.day) < (m, d))
            days_alive = (today - birth).days

            next_bday = date(today.year, m, d)
            if next_bday < today:
                next_bday = date(today.year + 1, m, d)

            days_until = (next_bday - today).days

            print("\nYour birthdate:", birth.strftime("%d / %m / %Y"))
            print("Your age:", age)
            print("You have been alive for", days_alive, "days")
            print("That is", days_alive * 24, "hours")

            if days_until == 0:
                print(f"\n🎈 Happy {ordinal(age)} birthday! 🎈")
            else:
                print("\nYour next birthday is in:", days_until, "days")
            break

        except ValueError:
            print("Invalid Input. Please try again.")


def days_until_event():
    print("\nDays Until Event")

    event = input("What is the event?: ").strip()

    try:
        d = int(input("Day (1-31): "))
        m = int(input("Month (1-12): "))
        y = int(input("Year (YYYY): "))

        today = date.today()
        event_date = date(y, m, d)
        diff = (event_date - today).days

        if diff < 0:
            print(f"\nThe event '{event}' has already passed.")
        elif diff == 0:
            print(f"\nToday is the day of '{event}'!")
        else:
            print(f"\nThere are {diff} days until '{event}'.")

    except ValueError:
        print("\nInvalid date entered.")


def number_guessing_game():
    print("\nNumber Guessing Game")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < secret:
                print("Too low.\n")
            elif guess > secret:
                print("Too high.\n")
            else:
                print(f"\nCorrect! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.\n")


def calculator():
    print("\nCalculator")

    try:
        a = float(input("Enter 1st number: "))
        op = input("Choose operation (+, -, *, /): ").strip()
        b = float(input("Enter 2nd number: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("Cannot divide by zero.")
                return
            result = a / b
        else:
            print("Invalid operation.")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid number entered.")


def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Birthday program")
        print("2. Days until event")
        print("3. Number guessing game")
        print("4. Calculator")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            birthday_program()
        elif choice == "2":
            days_until_event()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            calculator()
        elif choice == "5":
            print("Goodbye! Have a good day!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
