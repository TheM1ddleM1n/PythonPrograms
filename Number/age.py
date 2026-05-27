try:
    age = int(input("Please input your age "))

    if age >= 16:
        print("\nCongrats! You're old enough to participate.")
    else:
        print("\nSorry, you're still too young. Come back when you're 16 or older!")

except ValueError:
    print("\nOops! Please enter a valid number for your age.")

input("\nPress Enter to exit.")
