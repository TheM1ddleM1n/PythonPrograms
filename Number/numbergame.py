SECRET = 777

print("In this program you will need to guess the number I am thinking of")
print("I am thinking of a number between 1 and 800")

while True:
    try:
        guess = int(input())

        if guess < SECRET:
            print("Your guess is too low! Please try again.")
        elif guess > SECRET:
            print("Your guess is too high! Please try again.")
        else:
            print("Well done!! Your guess is correct!")
            break
    except ValueError:
        print("Please enter a valid number.")
