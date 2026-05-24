def number_validation():
    number = int(input("Enter a number between 1 and 30 (inclusive): "))
    while number < 1 or number > 30:
        print("Invalid!")
        number = int(input("Enter a number between 1 and 30 (inclusive): "))
    print("Thank you that was correct!")


def password_verification():
    password1 = input("Choose a new password: ")
    password2 = input("Please re-enter to verify: ")

    while password1 != password2:
        print("Passwords do not match, please try again.")
        password1 = input("Choose a new password: ")
        password2 = input("Please re-enter to verify: ")

    print("Password was set successfully!")


def print_python_is_great():
    for s in range(100):  # prints 100 times
        print("Python Is Great!")


def counting_loop():
    count = 1
    while count < 1001:
        print("The count is", count)
        count += 1


def print_sentence_chars():
    string = input("Please enter your own sentence: ")
    for x in string:
        print(x)


def to_infinity():
    max_count = int(input("Enter how many times to print the infinity message: "))
    x = 1
    while x <= max_count:
        print(f"To infinity and beyond! We are getting close, on {x} now!")
        x += 1


def main():
    while True:
        print("\n" + "=" * 40)
        print("LOOPS PROGRAM")
        print("=" * 40)
        print("1. Number validation 😊")
        print("=" * 40)
        print("2. Password verification")
        print("=" * 40)
        print("3. Print 'Python Is Great!' 100 times")
        print("=" * 40)
        print("4. Counting loop (from 1 to 1000!)")
        print("=" * 40)
        print("5. Print each character of a sentence")
        print("=" * 40)
        print("6. Safe 'To infinity' loop")
        print("=" * 40)
        print("7. Quit")
        print("=" * 40)

        choice = input("Enter the number of the program to run: ")

        if choice == "1":
            number_validation()
        elif choice == "2":
            password_verification()
        elif choice == "3":
            print_python_is_great()
        elif choice == "4":
            counting_loop()
        elif choice == "5":
            print_sentence_chars()
        elif choice == "6":
            to_infinity()
        elif choice == "7":
            print("Exiting Loops Program. Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1-7.")


if __name__ == "__main__":
    main()
