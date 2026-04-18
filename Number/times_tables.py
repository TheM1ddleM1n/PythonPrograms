def get_number():
    while True:
        try:
            num = int(input("Enter a number to display its multiplication table: "))
            return num
        except ValueError:
            print(
                "❌ Oops! That was a invalid input. Please try again with a valid integer."
            )


def display_table(num):
    print(f"\nMultiplication Table for {num}:\n")
    for i in range(1, 11):
        print(f"{num:>2} × {i:>2} = {num * i:>3}")
    print("\nDone!")


if __name__ == "__main__":
    number = get_number()
    display_table(number)
