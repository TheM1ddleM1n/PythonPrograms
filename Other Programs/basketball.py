"""Basketball game simulator with team scoring."""

import random


class Team:
    """Represents a basketball team."""
    
    def __init__(self, name):
        """Initialize team with name and score."""
        self.name = name
        self.score = 0


class Game:
    """Controls the basketball game."""
    
    def __init__(self):
        """Initialize game with two teams and quarter tracking."""
        self.home_team = Team("Home Team")
        self.away_team = Team("Away Team")
        self.quarter = 1

    def start_game(self):
        """Print game start message."""
        print(f"Game started! {self.home_team.name} vs. {self.away_team.name}")

    def quarter_over(self):
        """Handle end of quarter."""
        if self.quarter == 4:
            print("Game over!")
        else:
            self.quarter += 1
            print(f"End of Quarter {self.quarter}")

    def play_quarter(self):
        """Simulate one quarter of play."""
        for _ in range(5):  # Play 5 possessions per quarter
            home_score = random.randint(0, 5)
            away_score = random.randint(0, 5)
            self.home_team.score += home_score
            self.away_team.score += away_score
            print(f"{self.home_team.name}: {home_score} - {self.away_team.name}: {away_score}")

    def print_scores(self):
        """Print current scores (FIXED BUG)."""
        print(f"Current scores: {self.home_team.name} - {self.home_team.score}, "
              f"{self.away_team.name} - {self.away_team.score}")


def main():
    """Main game loop."""
    game = Game()
    while True:
        user_input = input("Press 'q' to quit, or press Enter to continue: ")
        if user_input == 'q':
            break
        game.start_game()
        game.play_quarter()
        game.quarter_over()
        game.print_scores()


if __name__ == "__main__":
    main()
