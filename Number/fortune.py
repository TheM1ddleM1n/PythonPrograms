import random
import time

FORTUNES = [
    "This is your lucky day — you are going to win the lottery!",
    "The sun is going to shine during your holidays!",
    "Congratulations! You bought a flashy car with your lottery money!",
    "Congratulations! You also bought a mansion with your money!",
    "Oh nooooo! You are bankrupt — you spent too much money on the economy. What do you do now?"
]

RARE_FORTUNES = [
    "The universe bends in your favour. This message appears once in a lifetime.",
    "You are chosen. Great power (and great responsibility) awaits you.",
    "Time slows. A decision you make soon will change everything."
]

def get_fortune(previous=None):
    roll = random.randint(1, 100) # every 1 in 100 rolls

    # 1% chance to get a 1
    if roll == 1:
        return random.choice(RARE_FORTUNES), True

    # Normal fortune
    fortune = random.choice(FORTUNES)
    while fortune == previous:
        fortune = random.choice(FORTUNES)

    return fortune, False

def main():
    print("Welcome to TheM1ddleM1n fortune teller v2")

    count = 0
    last_fortune = None

    while True:
        choice = input("\nWould you like your fortune read? (press y for yes, and q for quit): ").strip().lower()

        if choice in ("q", ""):
            break
        if choice != "y":
            print("Invalid input.")
            continue

        print("\nConsulting the ghostly spirits...")
        time.sleep(2.5)

        fortune, rare = get_fortune(last_fortune)

        if rare:
            print("\nA RARE FORTUNE HAS BEEN UNLOCKED!!!")
        else:
            last_fortune = fortune

        print(f"\n{fortune}")
        count += 1

    print(f"You had {count} fortune(s) read.")
    print(f"--------------------------")
    print(f"Goodbye!")

if __name__ == "__main__":
    main()
