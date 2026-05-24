import random
import time
import os

COUNTRIES_NORMAL = [
    ("Spain", "Europe"),
    ("US", "America"),
    ("UK", "Europe"),
    ("Poland", "Europe"),
    ("France", "Europe"),
    ("Australia", "Oceania"),
    ("Italy", "Europe"),
    ("Portugal", "Europe"),
    ("Finland", "Europe"),
    ("Scotland", "Europe"),
]

COUNTRIES_HARD = COUNTRIES_NORMAL + [
    ("Indonesia", "Asia"),
    ("India", "Asia"),
    ("Japan", "Asia"),
    ("Germany", "Europe"),
    ("Denmark", "Europe"),
    ("Algeria", "Africa"),
    ("Iceland", "Europe"),
    ("Ukraine", "Europe"),
    ("Greece", "Europe"),
    ("Ireland", "Europe"),
]

WRONG_PHRASES = [
    "That was an interesting guess, but not quite.",
    "That was not right :(",
    "Nice guess, but it's not this one.",
    "Nuh uh",
    "Wrong guess",
]

WON_PHRASES = [
    "You won!",
    "Congratulations, you guessed it right!",
    "GGs, you guessed it right!",
]


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    print("In this program you will need to guess the country I am thinking of")
    print("\n\nDifficulties:")
    print("1. Normal")
    print("2. Hard\n\n")

    difficulty = int(input("Please choose difficulty: "))
    clear()

    pool = COUNTRIES_HARD if difficulty >= 2 else COUNTRIES_NORMAL
    country, region = random.choice(pool)
    wrong_guesses = 0

    if difficulty < 2:
        print(f"I am thinking of a country in {region}. Good luck.")
    else:
        print("I am thinking of a country between the US and Japan. Good luck.")

    while True:
        guess = input("Please enter your guess: ")

        if guess.lower() != country.lower():
            wrong_guesses += 1
            print(random.choice(WRONG_PHRASES))
        else:
            if wrong_guesses > 5:
                print("It's not that one you noob")
                time.sleep(2)
                print("Nah just kidding you got it right")
            else:
                print(random.choice(WON_PHRASES))
            input()
            break


if __name__ == "__main__":
    main()
