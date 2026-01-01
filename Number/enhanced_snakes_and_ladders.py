"""Enhanced Snakes and Ladders!"""
import random


def roll_dice() -> int:
    """Roll a standard six-sided dice.
    
    Returns:
        Random integer between 1 and 6
    """
    return random.randint(1, 6)


def check_ladder(square: int, ladders: dict[int, int]) -> tuple[bool, int]:
    """Check if player landed on a ladder.
    
    Args:
        square: Current square position
        ladders: Dictionary mapping ladder start to ladder end
        
    Returns:
        Tuple of (landed_on_ladder, new_position)
    """
    if square in ladders:
        return True, ladders[square]
    return False, square


def check_snake(square: int, snakes: dict[int, int]) -> tuple[bool, int]:
    """Check if player landed on a snake.
    
    Args:
        square: Current square position
        snakes: Dictionary mapping snake head to snake tail
        
    Returns:
        Tuple of (landed_on_snake, new_position)
    """
    if square in snakes:
        return True, snakes[square]
    return False, square


def play_snakes_and_ladders():
    """Play the enhanced version of Snakes and Ladders."""
    # Define board layout
    ladders = {
        8: 23,
        21: 23,
        24: 29,
        54: 60
    }
    
    snakes = {
        10: 5,
        15: 10,
        30: 22,
        31: 26,
        63: 3
    }
    
    current_square = 0
    winning_square = 100
    turn_count = 0
    
    print('🎲 Welcome to Enhanced Snakes and Ladders!')
    print(f'Be the first to reach square {winning_square}!')
    print()
    
    while current_square < winning_square:
        input('Press Enter to roll the dice...')
        dice_roll = roll_dice()
        turn_count += 1
        print(f'🎲 Turn {turn_count}: You rolled a {dice_roll}')
        
        current_square += dice_roll
        
        # Check if player overshot the winning square
        if current_square > winning_square:
            print(f'⚠️ You rolled too high! Stay on square {current_square - dice_roll}')
            current_square -= dice_roll
            print()
            continue
        
        print(f'📍 You moved to square {current_square}')
        
        # Check for ladder
        is_ladder, new_square = check_ladder(current_square, ladders)
        if is_ladder:
            print(f'🪜 Ladder! You climb from {current_square} to {new_square}!')
            current_square = new_square
        
        # Check for snake
        is_snake, new_square = check_snake(current_square, snakes)
        if is_snake:
            print(f'🐍 Snake! You slide from {current_square} down to {new_square}!')
            current_square = new_square
        
        print()
    
    print('🎉 Congratulations! You reached square 100 and won the game!')
    print(f'🏁 You completed the game in {turn_count} turns!')


if __name__ == "__main__":
    play_snakes_and_ladders()
