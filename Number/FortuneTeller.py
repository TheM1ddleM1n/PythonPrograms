import random

fortune = 0
replay = "y"

print('Welcome to TheM1ddleM1n\'s fortune telling program!')
replay = input('Do you want to have your fortune read? Enter the key "y" to play on or press the "enter" key to exit: ')

while replay == "y":
    fortune = random.randint(1, 5)

    if fortune == 1:
        print('This is your lucky day, you are going to win the lottery!')
        replay = input('Do you want to play again? Enter y to play again or press enter to exit: ')
        print()

    elif fortune == 2:
        print('It is going to rain all holiday! What do you do now??')
        replay = input('Do you want to play again? Enter y to play again or press enter to exit: ')
        print()

    elif fortune == 3:
        print('Congratulations! You bought a flashy car with you lottery money!')
        replay = input('Do you want to play again? Enter y to play again or press enter to exit: ')
        print()

    elif fortune == 4:
        print('Congratulations! You also bought a mansion with your money. Very nice :)')
        replay = input('Do you want to play again? Enter y to play again or press enter to exit: ')
        print()

    elif fortune == 5:
        print('Oh noooooo! You are bankrupt you spent too much money. What do you do now??')
        replay = input('Do you want to play again? Enter y to play again or press enter to exit: ')
        print()
