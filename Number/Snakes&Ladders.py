"""
Unified Snakes and Ladders Game
Combines all 3 versions with multiple game modes
"""
import random
from typing import Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class GameMode(Enum):
    """Available game modes."""
    SINGLE_PLAYER = "1"
    TWO_PLAYER = "2"
    CLASSIC = "classic"
    ENHANCED = "enhanced"


@dataclass
class BoardConfig:
    """Game board configuration."""
    winning_square: int = 100
    ladders: Dict[int, int] = None
    snakes: Dict[int, int] = None
    
    def __post_init__(self):
        if self.ladders is None:
            self.ladders = {
                8: 23,
                21: 23,
                24: 29,
                54: 60
            }
        if self.snakes is None:
            self.snakes = {
                10: 5,
                15: 10,
                30: 22,
                31: 26,
                63: 3
            }


class Player:
    """Represents a player in the game."""
    
    def __init__(self, name: str, player_number: int = 1):
        self.name = name
        self.number = player_number
        self.position = 0
        self.turns = 0
    
    def move(self, spaces: int, board: BoardConfig) -> Tuple[int, Optional[str]]:
        """
        Move player and handle overshooting.
        
        Returns:
            Tuple of (new_position, event_message)
        """
        new_pos = self.position + spaces
        event = None
        
        # Check for overshoot
        if new_pos > board.winning_square:
            event = f"⚠️ Rolled too high! Stay on square {self.position}"
            return self.position, event
        
        self.position = new_pos
        self.turns += 1
        
        # Check for ladder
        if self.position in board.ladders:
            old_pos = self.position
            self.position = board.ladders[self.position]
            event = f"🪜 Ladder! Climbed from {old_pos} to {self.position}"
        
        # Check for snake
        elif self.position in board.snakes:
            old_pos = self.position
            self.position = board.snakes[self.position]
            event = f"🐍 Snake! Slid from {old_pos} down to {self.position}"
        
        return self.position, event
    
    def has_won(self, board: BoardConfig) -> bool:
        """Check if player has won."""
        return self.position >= board.winning_square


class SnakesAndLaddersGame:
    """Main game controller."""
    
    def __init__(self, num_players: int = 1):
        self.board = BoardConfig()
        self.players = []
        
        if num_players == 1:
            self.players.append(Player("Player", 1))
        else:
            for i in range(num_players):
                self.players.append(Player(f"Player {i+1}", i+1))
        
        self.current_player_idx = 0
        self.game_over = False
    
    def roll_dice(self) -> int:
        """Roll a six-sided die."""
        return random.randint(1, 6)
    
    def get_current_player(self) -> Player:
        """Get the current player."""
        return self.players[self.current_player_idx]
    
    def next_player(self):
        """Move to next player."""
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
    
    def play_turn(self) -> Tuple[Player, int, Optional[str]]:
        """
        Play one turn.
        
        Returns:
            Tuple of (player, dice_roll, event_message)
        """
        player = self.get_current_player()
        
        input(f"\n{player.name}, press Enter to roll the dice...")
        
        dice_roll = self.roll_dice()
        print(f"🎲 {player.name} rolled a {dice_roll}")
        
        old_pos = player.position
        new_pos, event = player.move(dice_roll, self.board)
        
        if new_pos != old_pos:
            print(f"📍 Moved to square {new_pos}")
        
        if event:
            print(event)
        
        if player.has_won(self.board):
            self.game_over = True
            return player, dice_roll, "WON"
        
        self.next_player()
        return player, dice_roll, event
    
    def show_status(self):
        """Display current game status."""
        print("\n" + "=" * 50)
        for player in self.players:
            print(f"{player.name}: Square {player.position}")
        print("=" * 50)
    
    def play(self):
        """Main game loop."""
        print("\n🎲 Welcome to Snakes and Ladders!")
        print(f"First to reach square {self.board.winning_square} wins!\n")
        
        while not self.game_over:
            self.play_turn()
            
            if len(self.players) > 1:
                self.show_status()
        
        winner = self.get_current_player()
        print(f"\n🎉 {winner.name} wins in {winner.turns} turns!")


def show_menu() -> GameMode:
    """Display game mode selection menu."""
    print("\n" + "=" * 50)
    print("🎲 SNAKES AND LADDERS")
    print("=" * 50)
    print("Choose game mode:")
    print("1. Single Player")
    print("2. Two Player")
    print("=" * 50)
    
    while True:
        choice = input("Enter choice (1-2): ").strip()
        if choice in ["1", "2"]:
            return GameMode(choice)
        print("❌ Invalid choice. Please enter 1 or 2.")


def main():
    """Main entry point."""
    mode = show_menu()
    
    if mode == GameMode.SINGLE_PLAYER:
        game = SnakesAndLaddersGame(num_players=1)
    else:
        game = SnakesAndLaddersGame(num_players=2)
    
    game.play()
    
    # Ask to play again
    play_again = input("\n🔁 Play again? (y/n): ").strip().lower()
    if play_again == 'y':
        main()
    else:
        print("\n👋 Thanks for playing!")


if __name__ == "__main__":
    main()
