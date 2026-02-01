import random

# =============================
# 🎮 Game Constants & Settings
# =============================
RACE_LENGTH = 50

# ✅ Upgrade Progress Tracking
upgrades = {
    "Speed Enhancer": False,
    "Hazard Armor": False,
    "Turbo Capacitor": False
}

# 📊 Game Stats
progress = {
    "wins": 0,
    "rivals_defeated": 0,
    "story_unlocked": []
}

# =============================
# 📁 Save/Load Upgrade Progress
# =============================
def save_progress(upgrades, filename="drift_save.txt"):
    """Save upgrade progress to file."""
    with open(filename, "w") as f:
        for key, value in upgrades.items():
            f.write(f"{key}:{value}\n")


def load_progress(filename="drift_save.txt"):
    """Load upgrade progress from file."""
    try:
        with open(filename, "r") as f:
            for line in f:
                key, val = line.strip().split(":")
                upgrades[key] = val == "True"
    except FileNotFoundError:
        pass


# =============================
# 🛞 Track Generator
# =============================
def generate_track(length):
    """Generate random track terrain."""
    terrain = []
    for _ in range(length):
        roll = random.random()
        if roll < 0.1:
            terrain.append("~")  # Windy
        elif roll < 0.2:
            terrain.append("#")  # Slippery
        elif roll > 0.95:
            terrain.append("=")  # Power Strip
        else:
            terrain.append("*")  # Normal
    return terrain


# =============================
# 🧑‍💻 Rival ASCII Intro
# =============================
def rival_intro(name, taunt):
    """Display rival introduction."""
    print(f"\n🔥 New Challenger: {name}")
    print(f"{taunt}")
    print("""
  ____        _       
 |  _ \\ _   _| |_ ___ 
 | |_) | | | | __/ _ \\
 |  __/| |_| | ||  __/
 |_|    \\__,_|\\__\\___|
""")


# =============================
# 🎁 Upgrade Unlock Mechanic
# =============================
def award_upgrade():
    """Award a random upgrade to player."""
    upgrade_names = list(upgrades.keys())
    won_upgrade = random.choice(upgrade_names)
    if not upgrades[won_upgrade]:
        upgrades[won_upgrade] = True
        print(f"🎉 Upgrade unlocked: {won_upgrade}!")
    else:
        print("🔁 Duplicate upgrade. Tough luck.")


# =============================
# 🧱 Hazards & Boosts (FIXED)
# =============================
def random_event():
    """Generate random hazard or boost event."""
    roll = random.random()
    if roll < 0.1:
        if upgrades["Hazard Armor"]:
            print("🛡️ Hazard dodged thanks to armor!")
            return 0
        print("💥 You hit an oil slick! Lose distance.")
        return -3
    elif roll > 0.9:
        if upgrades["Turbo Capacitor"]:
            print("🚀 TURBO BOOST activated! Zoom ahead.")
            return 5
    return 0


# =============================
# 📊 Visual Track
# =============================
def show_track(pos):
    """Display player position on track."""
    return "-" * pos + "🚗"


# =============================
# 🏁 Race Loop Begins (FIXED TERRAIN LOGIC)
# =============================
def race():
    """Main race game loop."""
    global progress
    load_progress()

    print("Choose your racer:")
    print("1. Drift King 🚗 (High speed, low control)")
    print("2. Balanced Rider 🚙 (Average speed & control)")
    print("3. Safe Driver 🚕 (Low speed, high control)")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        player_speed = (4, 8)
        hazard_chance = 0.3
    elif choice == "2":
        player_speed = (3, 6)
        hazard_chance = 0.2
    else:
        player_speed = (2, 5)
        hazard_chance = 0.1

    if upgrades["Speed Enhancer"]:
        player_speed = (player_speed[0] + 1, player_speed[1] + 1)

    terrain = generate_track(RACE_LENGTH)
    player_pos = 0
    cpu_pos = 0

    rival_intro("HexByte", "I debugged the racetrack. You're toast.")

    print("\n🏁 Race begins! First to reach 50 wins.\n")

    while player_pos < RACE_LENGTH and cpu_pos < RACE_LENGTH:
        move = input("Your move (accelerate/brake/boost): ").lower()
        tile = terrain[min(player_pos, RACE_LENGTH - 1)]

        # FIXED: Terrain effects now handled properly
        terrain_effect = 0
        if tile == "~":
            terrain_effect = -1
            print("🌪️ Windy section! Reduced boost effectiveness.")
        elif tile == "#":
            if random.random() < hazard_chance:
                print("⚠️ Slippery terrain! Lost control!")
                terrain_effect = -2
        elif tile == "=":
            print("💎 Power Strip! Instant boost!")
            terrain_effect = 3

        # Player Turn
        if move == "accelerate":
            gain = random.randint(*player_speed) + random_event() + terrain_effect
            player_pos += max(0, gain)  # Prevent negative position
        elif move == "brake":
            player_pos += 1
            print("🛑 You take it slow and steady.")
        elif move == "boost":
            gain = random.randint(2, 8) + random_event() + terrain_effect
            print("🎲 Risky boost move!")
            player_pos += max(0, gain)  # FIXED: Prevent negative
        else:
            print("❌ Invalid move. You stall.")
            continue

        # CPU Turn
        cpu_pos += random.randint(3, 6)

        # Display track
        print(f"\nTrack: {''.join(terrain)}")
        print(f"You:  {show_track(player_pos)} ({player_pos})")
        print(f"CPU:  {show_track(cpu_pos)} ({cpu_pos})\n")

    # Endgame
    if player_pos >= RACE_LENGTH and cpu_pos >= RACE_LENGTH:
        print("💨 It's a photo finish... DRAW!")
    elif player_pos >= RACE_LENGTH:
        print("🏆 YOU WIN THE RACE!")
        progress["wins"] += 1
        progress["rivals_defeated"] += 1
        award_upgrade()
    else:
        print("☠️ CPU wins! You'll get 'em next time.")

    save_progress(upgrades)


# =============================
# 🚗 Start the Game!
# =============================
race()
