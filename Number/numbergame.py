import os
import random
MAX_NUMBER = None

def clear():
  if os.name == "nt":
     os.system('cls')
  else:
     os.system('clear')
try:
   CHOICE = int(input("Choose a difficulty between 1 and 3: "))
   clear()
except ValueError:
   print("Invalid Choice")
   input()
   sys.exit()
if CHOICE == 3:
   MAX_NUMBER = 2000
if CHOICE == 2:
   MAX_NUMBER = 1500
if CHOICE == 1:
   MAX_NUMBER = 1000
if MAX_NUMBER == None:
   print("Invalid Choice")
   input()
   sys.exit()
   
SECRET = random.randint(1,MAX_NUMBER)

print("In this program you will need to guess the number I am thinking of")
print(f"I am thinking of a number between 1 and {MAX_NUMBER}")

while True:
    try:
        guess = int(input())
        if guess < SECRET:
            print("Your guess is too low! Please try again.")
        elif guess > SECRET:
            print("Your guess is too high! Please try again.")
        else:
            print("Well done!! Your guess is correct!")
            input()
            break
    except ValueError:
        print("Please enter a valid number.")
