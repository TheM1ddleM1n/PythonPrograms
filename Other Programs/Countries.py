import random
import time
import os

def clear():
   if os.name == "nt":
      os.system('cls')
   else:
      os.system('clear')

print("In this program you will need to guess the country I am thinking of")

print("")
print("")

print("Difficulties:")
print("1. Normal")
print("2. Hard")
print("")
print("")

difficulty = input("Please choose difficulty: ")

difficultylevel = int(difficulty)
clear()
  
if difficultylevel < 2:
   randomcountry = random.randint(1, 10)
else:
   randomcountry = random.randint(1, 20)
wrongguesses = 0
if randomcountry == 1:
    country = "Spain"
    region = "Europe"

if randomcountry == 2:
    country = "US"
    region = "America"

if randomcountry == 3:
    country = "UK"
    region = "Europe"

if randomcountry == 4:
    country = "Poland"
    region = "Europe"

if randomcountry == 5:
    country = "France"
    region = "Europe"

if randomcountry == 6:
    country = "Australia"
    region = "Oceania"

if randomcountry == 7:
    country = "Italy"
    region = "Europe"

if randomcountry == 8:
    country = "Portugal"
    region = "Europe"

if randomcountry == 9:
    country = "Finland"
    region = "Europe"

if randomcountry == 10:
    country = "Scotland"
    region = "Europe"

if randomcountry == 11:
    country = "Indonesia"
    region = "Asia"

if randomcountry == 12:
    country = "India"
    region = "Asia"

if randomcountry == 13:
    country = "Japan"
    region = "Asia"

if randomcountry == 14:
    country = "Germany"
    region = "Europe"

if randomcountry == 15:
    country = "Denmark"
    region = "Europe"

if randomcountry == 16:
    country = "Algeria"
    region = "Africa"

if randomcountry == 17:
    country = "Iceland"
    region = "Europe"

if randomcountry == 18:
    country = "Ukraine"
    region = "Europe"

if randomcountry == 19:
    country = "Greece"
    region = "Europe"

if randomcountry == 20:
    country = "Ireland"
    region = "Europe"




if difficultylevel < 2:
   print(f"I am thinking of a country in {region}. Good luck.")
else:
   print("I am thinking of a country between the US and Japan. Good luck.")

while True:
    guess = input("Please enter your guess: ")

    if guess.lower() != country.lower():
        randomphrases = random.randint(1, 5)
        wrongguesses = wrongguesses + 1
        if randomphrases == 1:
            print("That was a interesting guess, but not quite.")
        if randomphrases == 2:
            print("That was not right :(")
        if randomphrases == 3:
            print("Nice guess, but it's not this one.")
        if randomphrases == 4:
            print("Nuh uh")
        if randomphrases == 5:
            print("Wrong guess")
    if guess.lower() == country.lower():
        wonrandomphrases = random.randint(1, 3)
        if wrongguesses > 5:
            print("It's not that one you noob")
            time.sleep(2)
            print("Nah just kidding you got it right")
            input()
            exit()

        if wonrandomphrases == 1:
            print("You won!")
            input()
            exit()
        if wonrandomphrases == 2:
            print("Congratulations, you guessed it right!")
            input()
            exit()

        if wonrandomphrases == 3:
            print("GGs, you guessed it right!")
            input()
            exit()
