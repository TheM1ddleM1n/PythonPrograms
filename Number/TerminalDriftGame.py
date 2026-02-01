"""
Terminal Racing Game - Terminal Drift

A competitive terminal-based racing game where you race against the CPU.
Features include dynamic difficulty, persistent upgrades, and a real competitive AI.
"""

import random
import os
from pathlib import Path
from typing import Tuple, Optional


class RaceConfig:
    """Game configuration and constants."""
    TRACK_LENGTH = 100
    SAVE_FILE = "drift_save.txt"
    
    UPGRADES = ["Speed Enhancer", "Hazard Armor", "Turbo Capacitor"]
    
    VEHICLE_STATS = {
        "drift_king": {"min_speed": 5, "max_speed": 9, "hazard_chance": 0.35},
        "balanced": {"min_speed": 4, "max_speed": 7, "hazard_chance": 0.2},
        "safe_driver": {"min_speed": 2, "max_speed": 5, "hazard_chance": 0.08}
    }
    
    TERRAIN = {
        "normal": "*",
        "windy": "~",
        "slippery": "#",
        "boost": "="
    }


class Racer:
    """Represents a racing competitor."""
    
    def __init__(self, name, is_cpu=False):
        """Initialize racer with name and position."""
        self.name = name
        self.position = 0
        self.is_cpu = is_cpu
        self.distance_this_turn = 0
        self.was_ahead = False
    
    def move(self, distance):
        """Move racer forward by distance."""
        self.distance_this_turn = distance
        self.position += max(0, distance)
    
    def is_finished(self, track_length):
        """Check if racer reached the finish line."""
        return self.position >= track_length
    
    def __str__(self):
        """String representation of racer."""
        return f"{self.name}: {self.position}"


class UpgradeManager:
    """Manages player upgrades and progression."""
    
    def __init__(self):
        """Initialize with no upgrades."""
        self.upgrades = {name: False for name in RaceConfig.UPGRADES}
    
    def has(self, name):
        """Check if player has an upgrade."""
        return self.upgrades.get(name, False)
    
    def unlock(self, name):
        """Unlock an upgrade. Returns True if new, False if duplicate."""
        if not self.has(name):
            self.upgrades[name] = True
            print(f"Upgrade unlocked: {name}")
            return True
        else:
            print(f"Already own: {name}")
            return False
    
    def save(self):
        """Persist upgrades to disk."""
        try:
            with open(RaceConfig.SAVE_FILE, "w") as f:
                for name, owned in self.upgrades.items():
                    f.write(f"{name}:{owned}\n")
        except IOError as e:
            print(f"Could not save progress: {e}")
    
    def load(self):
        """Load upgrades from disk."""
        path = Path(RaceConfig.SAVE_FILE)
        if not path.exists():
            return
        
        try:
            with open(RaceConfig.SAVE_FILE) as f:
                for line in f:
                    name, value = line.strip().split(":")
                    if name in self.upgrades:
                        self.upgrades[name] = value == "True"
        except (IOError, ValueError) as e:
            print(f"Could not load progress: {e}")


class TrackGenerator:
    """Creates randomized race tracks."""
    
    @staticmethod
    def generate(length):
        """Create track with random terrain."""
        track = []
        for _ in range(length):
            roll = random.random()
            
            if roll < 0.08:
                track.append(RaceConfig.TERRAIN["windy"])
            elif roll < 0.15:
                track.append(RaceConfig.TERRAIN["slippery"])
            elif roll > 0.93:
                track.append(RaceConfig.TERRAIN["boost"])
            else:
                track.append(RaceConfig.TERRAIN["normal"])
        
        return track


class GamePhysics:
    """Handles game mechanics and interactions."""
    
    def __init__(self, upgrades):
        """Initialize physics engine with upgrade manager."""
        self.upgrades = upgrades
    
    def get_terrain_effect(self, terrain_tile):
        """Calculate speed effect from terrain."""
        if terrain_tile == "~":
            print("  Windy section! Struggling with crosswinds...")
            return -1
        elif terrain_tile == "#":
            print("  Slippery road! Hydroplaning!")
            return -2
        elif terrain_tile == "=":
            print("  Power strip! Instant acceleration!")
            return 4
        return 0
    
    def process_hazard(self):
        """Generate random hazard or boost."""
        roll = random.random()
        
        if roll < 0.09:
            if self.upgrades.has("Hazard Armor"):
                print("  Armor protected you from the crash!")
                return 0
            print("  Collision! Hit an obstacle!")
            return -4
        
        if roll > 0.82:
            if self.upgrades.has("Turbo Capacitor"):
                print("  Turbo kicked in!")
                return 6
        
        return 0
    
    def get_speed_bonus(self, vehicle_type):
        """Calculate speed range with upgrade bonus."""
        stats = RaceConfig.VEHICLE_STATS[vehicle_type]
        min_speed = stats["min_speed"]
        max_speed = stats["max_speed"]
        
        if self.upgrades.has("Speed Enhancer"):
            min_speed += 2
            max_speed += 2
        
        return min_speed, max_speed


class AIRacer:
    """CPU-controlled opponent with dynamic strategy."""
    
    def __init__(self):
        """Initialize AI with baseline stats."""
        self.aggression = random.uniform(0.4, 0.9)
        self.consistency = random.uniform(0.6, 0.95)
    
    def decide_action(self, player_ahead):
        """Choose action based on race state."""
        roll = random.random()
        
        if player_ahead and roll < self.aggression:
            return "boost"
        elif roll < 0.2:
            return "brake"
        else:
            return "accelerate"


class RaceGame:
    """Main game controller."""
    
    def __init__(self):
        """Initialize game state."""
        self.upgrades = UpgradeManager()
        self.upgrades.load()
        self.physics = GamePhysics(self.upgrades)
        self.stats = {"wins": 0, "races": 0, "best_margin": 0}
    
    def show_vehicle_selection(self):
        """Display vehicle menu and return selection."""
        print("\nSelect Your Vehicle:")
        print("  1. Drift King    - High speed, risky (5-9 per turn)")
        print("  2. Balanced      - Steady performance (4-7 per turn)")
        print("  3. Safe Driver   - Stable, lower speed (2-5 per turn)")
        print()
        
        while True:
            choice = input("Choice (1-3): ").strip()
            if choice in ["1", "2", "3"]:
                vehicles = {"1": "drift_king", "2": "balanced", "3": "safe_driver"}
                return vehicles[choice]
            print("Invalid. Try again.")
    
    def display_track_status(self, track, player, cpu):
        """Draw visual representation of race."""
        print("\n" + "-" * 60)
        print(f"Track: {''.join(track)}")
        print(f"Player:  {'>' * min(player.position, 50)}C ({player.position:3d})")
        print(f"CPU:     {'>' * min(cpu.position, 50)}C ({cpu.position:3d})")
        print("-" * 60)
    
    def get_player_action(self):
        """Get validated player input."""
        while True:
            action = input("Action (accelerate/brake/boost): ").strip().lower()
            if action in ["accelerate", "brake", "boost"]:
                return action
            print("Invalid action. Choose: accelerate, brake, or boost")
    
    def play_race(self):
        """Execute single race."""
        vehicle = self.show_vehicle_selection()
        min_speed, max_speed = self.physics.get_speed_bonus(vehicle)
        hazard_chance = RaceConfig.VEHICLE_STATS[vehicle]["hazard_chance"]
        
        track = TrackGenerator.generate(RaceConfig.TRACK_LENGTH)
        player = Racer("You", is_cpu=False)
        cpu = Racer("CPU", is_cpu=True)
        ai = AIRacer()
        
        print("\n" + "=" * 60)
        print("RACE START - First to 100 wins!")
        print("=" * 60)
        
        turn = 0
        
        while not player.is_finished(RaceConfig.TRACK_LENGTH) and \
              not cpu.is_finished(RaceConfig.TRACK_LENGTH):
            
            turn += 1
            print(f"\nTurn {turn}")
            print("-" * 60)
            
            # Player turn
            action = self.get_player_action()
            current_terrain = track[min(player.position, RaceConfig.TRACK_LENGTH - 1)]
            terrain_effect = self.physics.get_terrain_effect(current_terrain)
            hazard_effect = self.physics.process_hazard()
            
            if action == "accelerate":
                distance = random.randint(min_speed, max_speed) + terrain_effect + hazard_effect
                print(f"  Accelerating...")
            elif action == "brake":
                distance = 1
                print(f"  Braking... conservative but safe.")
            else:  # boost
                distance = random.randint(3, 10) + terrain_effect + hazard_effect
                print(f"  Risky boost maneuver!")
            
            player.move(distance)
            print(f"  Traveled: {max(0, distance)} spaces")
            
            # CPU turn
            player_ahead = player.position > cpu.position
            cpu_action = ai.decide_action(player_ahead)
            cpu_terrain = track[min(cpu.position, RaceConfig.TRACK_LENGTH - 1)]
            cpu_terrain_effect = self._get_cpu_terrain_effect(cpu_terrain)
            cpu_hazard = random.randint(-3, 4)
            
            if cpu_action == "boost":
                cpu_distance = random.randint(4, 9) + cpu_terrain_effect + cpu_hazard
            elif cpu_action == "brake":
                cpu_distance = 1
            else:
                cpu_distance = random.randint(3, 7) + cpu_terrain_effect + cpu_hazard
            
            cpu.move(cpu_distance)
            
            # Check if CPU just passed player
            if not player.was_ahead and cpu.position > player.position:
                print("\n  CPU: Eat my dust!")
                cpu.was_ahead = True
            elif player.was_ahead and player.position > cpu.position:
                print("\n  You take the lead!")
                player.was_ahead = True
            
            self.display_track_status(track, player, cpu)
        
        # End race
        self.stats["races"] += 1
        self._handle_race_end(player, cpu)
    
    def _get_cpu_terrain_effect(self, terrain):
        """Simplified terrain effect for CPU."""
        if terrain == "~":
            return -1
        elif terrain == "#":
            return random.randint(-2, 0)
        elif terrain == "=":
            return 2
        return 0
    
    def _handle_race_end(self, player, cpu):
        """Process race results."""
        print("\n" + "=" * 60)
        print("RACE OVER")
        print("=" * 60)
        
        if player.position >= RaceConfig.TRACK_LENGTH and \
           cpu.position >= RaceConfig.TRACK_LENGTH:
            print("Photo finish! It's a dead heat!")
        elif player.position >= RaceConfig.TRACK_LENGTH:
            margin = player.position - cpu.position
            self.stats["wins"] += 1
            self.stats["best_margin"] = max(self.stats["best_margin"], margin)
            print(f"Victory! You won by {margin} spaces.")
            self._award_upgrade()
        else:
            margin = cpu.position - player.position
            print(f"Defeat. CPU won by {margin} spaces.")
        
        self.upgrades.save()
    
    def _award_upgrade(self):
        """Award random upgrade to player."""
        upgrade = random.choice(RaceConfig.UPGRADES)
        self.upgrades.unlock(upgrade)
    
    def show_stats(self):
        """Display career statistics."""
        print("\n" + "=" * 60)
        print("CAREER STATISTICS")
        print("=" * 60)
        print(f"Races completed: {self.stats['races']}")
        print(f"Wins: {self.stats['wins']}")
        if self.stats['races'] > 0:
            win_rate = (self.stats['wins'] / self.stats['races']) * 100
            print(f"Win rate: {win_rate:.1f}%")
        if self.stats['best_margin'] > 0:
            print(f"Best victory margin: {self.stats['best_margin']} spaces")
        
        print("\nUpgrades unlocked:")
        for upgrade, owned in self.upgrades.upgrades.items():
            status = "Owned" if owned else "Locked"
            print(f"  {upgrade}: {status}")
        print("=" * 60)
    
    def run(self):
        """Main game loop."""
        print("\n" + "=" * 60)
        print("TERMINAL DRIFT RACING")
        print("=" * 60)
        print("Compete against the CPU, unlock upgrades, and become champion.")
        print()
        
        while True:
            print("\nMenu:")
            print("  1. Start race")
            print("  2. View stats")
            print("  3. Exit")
            print()
            
            choice = input("Choice (1-3): ").strip()
            
            if choice == "1":
                self.play_race()
            elif choice == "2":
                self.show_stats()
            elif choice == "3":
                print("Thanks for playing. Goodbye.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    game = RaceGame()
    game.run()
