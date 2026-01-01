# Number data types
import random

# Subroutine to generate a random number from 1-6
def RollDice():
    return random.randint(1,6)

# Main program!
random.seed()
Dice = RollDice()
print("You rolled a {}".format(Dice))
