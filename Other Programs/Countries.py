import random
import time

randomcountry = random.randint(1, 10)
wrongguesses = 0
if randomcountry == 1:
    country = "Spain"

if randomcountry == 2:
    country = "US"

if randomcountry == 3:
    country = "UK"

if randomcountry == 4:
    country = "Poland"

if randomcountry == 5:
    country = "France"

if randomcountry == 6:
    country = "Australia"

if randomcountry == 7:
    country = "Italy"

if randomcountry == 8:
    country = "Portugal"

if randomcountry == 9:
    country = "Finland"

if randomcountry == 10:
    country = "Scotland"

print("In this program you will need to guess the country I am thinking of")
print("I am thinking of a country between London and Japan. Good luck.")

while True:
    guess = input("Please enter your guess: ")

    if guess.lower() != country.lower():
        randomphrases = random.randint(1, 5)
        wrongguesses = wrongguesses + 1
        if randomphrases == 1:
            print("That was a interesting guess, but not quite.")
        if randomphrases == 2:
            print("Welp. That was not right :(")
        if randomphrases == 3:
            print("Nice guess, but it's not this one.")
        if randomphrases == 4:
            print("Nuh uh")
        if randomphrases == 5:
            print("Wrong guess")
    if guess.lower() == country.lower():
        wonrandomphrases = random.randint(1, 4)
        if wrongguesses > 5:
            print("It's not that one you noob")
            time.sleep(2)
            print("Nah just kidding you got it right")
            input()

        if wonrandomphrases == 1:
            print("You won!")
            input()
        if wonrandomphrases == 2:
            print("Congratulations, you guessed it right!")
            input()

        if wonrandomphrases == 4:
            print("GGs, you guessed it right!")
            input()
