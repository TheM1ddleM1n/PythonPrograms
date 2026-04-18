number = 777

print("In this program you will need to guess the number I am thinking of")

print("I am thinking of a number between 1 and 800")

while number == 777:
    guess = input()

    guess = int(guess)

    if guess < 777:
        print("Your guess is too low! Please try again.")

    if guess > 777:
        print("Your guess is too high! Please try again.")

    if guess == 777:
        print("Well done!! Your guess is correct!")

        break
