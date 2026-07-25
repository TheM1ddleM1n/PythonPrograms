import random
import sys
import time

def slow(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def pick_number(mode):
    if mode == "1":
        return random.randint(1, 50)

    if mode == "2":
        return random.randint(1, 100)

    if mode == "3":
        return random.randint(1, 500)

    if mode == "X":
        return random.randint(1, 1000)


def intro():
    slow("Welcome to NumberGuesser 1.0 !", 0.05)
    print()
    time.sleep(0.5)


def choose_mode():
    slow("Choose difficulty:")
    slow("1 = Easy")
    slow("2 = Normal")
    slow("3 = Hard")

    mode = input().strip().upper()

    if mode == "404":
        return "X"

    if mode in ("1", "2", "3"):
        return mode

    return choose_mode()


def play(mode):
    number = pick_number(mode)
    attempts = 0

    slow("Guess the number")

    while True:
        guess = input().strip()

        if not guess.isdigit():
            continue

        guess = int(guess)
        attempts += 1

        if guess > number:
            slow("Lower")

        elif guess < number:
            slow("Higher")

        else:
            slow("You won in " + str(attempts) + " attempts")
            break


def secret_reveal():
    slow("Secret mode unlocked")
    time.sleep(0.5)
    slow("Range increased")
    time.sleep(0.5)
    slow("Good luck")


while True:
    intro()

    mode = choose_mode()

    if mode == "X":
        secret_reveal()

    play(mode)

    slow("Play again? (y/n)")

    if input().strip().lower() != "y":
        break
input()
