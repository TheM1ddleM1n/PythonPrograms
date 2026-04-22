import time
import random

print("Welcome to NumberGuesser 1.0 !")
print("")
print("")
time.sleep(3)


number = random.randint(1,100)

while True:
 guess = int(input())
 if guess > number:
   print("Lower")
 if guess < number:
   print("Higher")
 if guess == number:
   print("You won !")
   break


time.sleep(1e6)

# Coded by XXXDark303