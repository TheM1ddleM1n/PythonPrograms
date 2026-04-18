import random

# Dictionary linking moods to song suggestions
mood_music = {
    "happy": [
        "Walking on Sunshine – Katrina & The Waves",
        "Can't Stop the Feeling – Justin Timberlake",
        "Electric Feel – MGMT",
        "Dancing Queen - ABBA",
        "24K Magic - Bruno Mars",
        "APT. - Rosé + Bruno Mars",
        "Don't Stop Me Now - Queen",
    ],
    "sad": [
        "Someone Like You – Adele",
        "Fix You – Coldplay",
        "The Night We Met – Lord Huron",
        "i dont wanna break - Christina Perri",
        "Man That's Never Known You - Zach Bryan",
        "Everglow - Coldplay",
        "Teddy Bear - Melanie Martinez",
        "When I Was Your Man - Bruno Mars",
    ],
    "angry": [
        "Killing In the Name – Rage Against The Machine",
        "DNA – Kendrick Lamar",
        "Smells Like Teen Spirit – Nirvana",
        "Damaged - Black Flag",
    ],
    "chill": [
        "Weightless – Marconi Union",
        "Coffee – Beabadoobee",
        "Sunflower – Rex Orange County",
    ],
    "romantic": [
        "All of Me – John Legend",
        "Yellow – Coldplay",
        "Lover – Taylor Swift",
    ],
    "motivated": [
        "Stronger – Kanye West",
        "Eye of the Tiger – Survivor",
        "Lose Yourself – Eminem",
    ],
}


def suggest_song(mood):
    mood = mood.lower()
    if mood in mood_music:
        song = random.choice(mood_music[mood])
        print(
            f"\nFeeling this {mood}? Here's a track for you that you might like: 🎶 {song}"
        )
    else:
        print("\nMood not recognized 😕 Try a mood like happy, chill, romantic, etc.")


def main():
    print("Welcome to MoodMusicSuggester!")
    mood = input("What is your current mood right now? ")
    suggest_song(mood)


if __name__ == "__main__":
    main()
