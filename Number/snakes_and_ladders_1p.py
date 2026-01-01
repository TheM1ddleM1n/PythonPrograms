"""Snakes and Ladders Game - Single Player!"""
import random

current_square = 0
print('Welcome to the Snakes and Ladders The GAME!')
print('You must reach square 100 to win this game.')

while current_square < 101:
    print('Roll the dice by pressing enter.')
    input()
    dice_roll = random.randint(1, 6)
    print(f'You rolled a {dice_roll}')
    current_square += dice_roll
    print(f'You are on square {current_square}')
    
    # Ladders
    if current_square == 8:
        print('Well done, go up the ladder to square 23')
        current_square += 15
    elif current_square == 54:
        print('Well done, go up the ladder to square 60')
        current_square = 60  # refractored: was adding 60 instead of setting to 60
    elif current_square == 24:
        print('Well done, go up the ladder to square 29')
        current_square += 5
    elif current_square == 21:
        print('Well done, go up the ladder to square 23')
        current_square += 2
    
    # Snakes
    if current_square == 10:
        print('Oh no, you have landed on a snake, go back five')
        current_square -= 5
    elif current_square == 15:
        print('Oh no, you have landed on a snake, go down 5 squares')
        current_square -= 5
    elif current_square == 30:
        print('Oh no, you have landed on a snake go down 8 spaces')
        current_square -= 8
    elif current_square == 31:
        print('Oh no, you have landed on a snake, go down five spaces')
        current_square -= 5
    elif current_square == 63:
        print('Oh no, you have landed on the biggest snake')
        current_square -= 60

print('🎉 Congratulations! You won!')
