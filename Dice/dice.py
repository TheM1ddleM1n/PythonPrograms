"""
Unified Dice Game Collection
Combines simple dice roller, ASCII display, and guessing game
"""
import random
from typing import Optional
from enum import Enum


class DiceMode(Enum):
    """Available dice game modes."""

    SIMPLE_ROLL = "1"
    ASCII_DISPLAY = "2"
    GUESSING_GAME = "3"


class DiceGame:
    """Unified dice game with multiple modes."""

    SEPARATOR = "=" * 50

    # Dice face Unicode characters
    DICE_FACES = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅",
    }

    # ASCII art for dice faces
    ASCII_DICE = {
        1: [
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ],
        2: [
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ],
        3: [
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ],
        4: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ],
        5: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ],
        6: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ],
    }

    def __init__(self):
        random.seed()

    def roll(self, sides: int = 6) -> int:
        """Roll a dice with specified number of sides."""
        return random.randint(1, sides)

    def get_unicode_face(self, value: int) -> str:
        """Get Unicode character for dice face."""
        return self.DICE_FACES.get(value, str(value))

    def display_ascii_dice(self, value: int):
        """Display ASCII art dice."""
        if value in self.ASCII_DICE:
            for line in self.ASCII_DICE[value]:
                print(line)
        else:
            print(f"Dice value: {value}")

    def simple_roll_mode(self):
        """Mode 1: Simple dice roller."""
        print("\n🎲 SIMPLE DICE ROLLER")
        print(self.SEPARATOR)

        while True:
            input("Press Enter to roll the dice (or 'q' + Enter to quit)...")

            roll = self.roll()
            print(f"\n🎲 You rolled a {roll} {self.get_unicode_face(roll)}\n")

            cont = (
                input("Roll again? (Enter to continue, 'q' to quit): ")
                .strip()
                .lower()
            )
            if cont == "q":
                break

    def ascii_display_mode(self):
        """Mode 2: ASCII art dice display."""
        print("\n🎲 ASCII DICE DISPLAY")
        print(self.SEPARATOR)

        while True:
            try:
                value = (
                    input(
                        "\nEnter dice value (1-6) or 'r' to roll randomly (q to quit): "
                    )
                    .strip()
                    .lower()
                )

                if value == "q":
                    break
                if value == "r":
                    value = self.roll()
                    print(f"\n🎲 Rolled: {value}")
                else:
                    value = int(value)
                    if not 1 <= value <= 6:
                        print("⚠️ Please enter a number between 1 and 6")
                        continue

                print()
                self.display_ascii_dice(value)

            except ValueError:
                print("❌ Invalid input. Please enter a number, 'r', or 'q'")

    def guessing_game_mode(self):
        """Mode 3: Advanced guessing game with difficulty levels."""
        print("\n🎲 DICE GUESSING GAME")
        print(self.SEPARATOR)

        player_name = input("\nEnter your name: ").strip() or "Player"

        print("\nChoose difficulty:")
        print("1. Easy (6-sided die)")
        print("2. Medium (12-sided die)")
        print("3. Hard (20-sided die)")

        difficulty_map = {
            "1": ("Easy", 6),
            "2": ("Medium", 12),
            "3": ("Hard", 20),
        }

        choice = input("Enter choice (1-3): ").strip()
        difficulty, sides = difficulty_map.get(choice, ("Easy", 6))

        print(f"\n🎮 Playing on {difficulty} mode with {sides}-sided die")

        rounds = 5
        score = 0

        for round_num in range(1, rounds + 1):
            print("\n" + self.SEPARATOR)
            print(f"🔁 Round {round_num}/{rounds}")
            print(self.SEPARATOR)

            while True:
                try:
                    guess = int(input(f"Guess the dice roll (1-{sides}): "))
                    if 1 <= guess <= sides:
                        break
                    print(f"⚠️ Please guess between 1 and {sides}")
                except ValueError:
                    print("❌ Please enter a valid number")

            roll = self.roll(sides)

            if sides <= 6:
                print(f"🎲 Dice rolled: {roll} {self.get_unicode_face(roll)}")
            else:
                print(f"🎲 Dice rolled: {roll}")

            if guess == roll:
                print("✅ Correct! +1 point")
                score += 1
            else:
                print("❌ Wrong! Better luck next time")

        print("\n" + self.SEPARATOR)
        print("🏁 GAME OVER!")
        print(self.SEPARATOR)
        print(f"Player: {player_name}")
        print(f"Final Score: {score}/{rounds}")
        print(f"Accuracy: {(score / rounds) * 100:.1f}%")

        if score == rounds:
            print("🏆 PERFECT! You're a dice master!")
        elif score >= rounds * 0.6:
            print("👏 Great job! Well done!")
        elif score >= rounds * 0.4:
            print("👍 Not bad! Keep practicing!")
        else:
            print("💪 Keep trying! You'll get better!")


def show_main_menu() -> Optional[DiceMode]:
    """Display main menu and get user choice."""
    print("\n" + "=" * 50)
    print("🎲 DICE GAME COLLECTION")
    print("=" * 50)
    print("1. Simple Dice Roller")
    print("2. ASCII Dice Display")
    print("3. Dice Guessing Game")
    print("4. Exit")
    print("=" * 50)

    choice = input("Enter choice (1-4): ").strip()

    if choice == "4":
        return None
    if choice in {"1", "2", "3"}:
        return DiceMode(choice)

    print("❌ Invalid choice. Please enter 1-4.")
    return show_main_menu()


def main():
    """Main entry point."""
    game = DiceGame()

    while True:
        mode = show_main_menu()

        if mode is None:
            print("\n👋 Thanks for playing!")
            break

        if mode == DiceMode.SIMPLE_ROLL:
            game.simple_roll_mode()
        elif mode == DiceMode.ASCII_DISPLAY:
            game.ascii_display_mode()
        elif mode == DiceMode.GUESSING_GAME:
            game.guessing_game_mode()


if __name__ == "__main__":
    main()
