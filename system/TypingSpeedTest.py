import time
import random


SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog near the riverbank.",
    "Python is a powerful programming language used for web development.",
    "Practice makes perfect when learning to type faster and more accurately.",
    "Technology continues to evolve at an incredible pace in the modern world.",
    "Coffee is the fuel that powers developers through long coding sessions.",
    "Learning new skills requires dedication persistence and a growth mindset.",
    "The internet has transformed how we communicate share and learn information.",
    "Artificial intelligence is reshaping industries and creating new opportunities.",
]


def calculate_wpm(text, time_taken):
    """Calculate words per minute."""
    words = len(text.split())
    minutes = time_taken / 60
    return round(words / minutes, 2) if minutes > 0 else 0


def calculate_accuracy(original, typed):
    """Calculate typing accuracy percentage."""
    correct = sum(1 for o, t in zip(original, typed) if o == t)
    total = max(len(original), len(typed))
    return round((correct / total) * 100, 2) if total > 0 else 0


def display_stats(wpm, accuracy, time_taken, errors):
    """Display test results."""
    print("\n" + "=" * 50)
    print("📊 RESULTS")
    print("=" * 50)
    print(f"⚡ Speed: {wpm} WPM")
    print(f"🎯 Accuracy: {accuracy}%")
    print(f"⏱️  Time: {time_taken:.2f} seconds")
    print(f"❌ Errors: {errors}")
    
    # Performance rating
    if wpm >= 60 and accuracy >= 95:
        print("\n🏆 Excellent! You're a typing master!")
    elif wpm >= 40 and accuracy >= 85:
        print("\n👍 Great job! Keep practicing!")
    elif wpm >= 25:
        print("\n💪 Good effort! Practice makes perfect!")
    else:
        print("\n🌱 Keep practicing, you'll improve!")


def typing_test():
    """Run a single typing test."""
    text = random.choice(SAMPLE_TEXTS)
    
    print("\n" + "=" * 50)
    print("Type the following text:")
    print("=" * 50)
    print(f"\n{text}\n")
    print("=" * 50)
    
    input("Press ENTER when ready to start...")
    print("\nGO! Start typing:\n")
    
    start_time = time.time()
    typed_text = input()
    end_time = time.time()
    
    time_taken = end_time - start_time
    wpm = calculate_wpm(text, time_taken)
    accuracy = calculate_accuracy(text, typed_text)
    
    # Count errors
    errors = sum(1 for o, t in zip(text, typed_text) if o != t)
    errors += abs(len(text) - len(typed_text))  # Add length difference
    
    display_stats(wpm, accuracy, time_taken, errors)
    
    return wpm, accuracy


def main():
    print("⌨️  Welcome to the Typing Speed Test!")
    print("Test your typing speed and accuracy")
    
    total_tests = 0
    total_wpm = 0
    total_accuracy = 0
    
    while True:
        print("\n" + "=" * 50)
        print("1. Start typing test")
        print("2. View overall stats")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == "1":
            wpm, accuracy = typing_test()
            total_tests += 1
            total_wpm += wpm
            total_accuracy += accuracy
            
        elif choice == "2":
            if total_tests == 0:
                print("\n❌ No tests completed yet!")
            else:
                avg_wpm = round(total_wpm / total_tests, 2)
                avg_accuracy = round(total_accuracy / total_tests, 2)
                print("\n" + "=" * 50)
                print("📈 OVERALL STATISTICS")
                print("=" * 50)
                print(f"Tests completed: {total_tests}")
                print(f"Average WPM: {avg_wpm}")
                print(f"Average Accuracy: {avg_accuracy}%")
                
        elif choice == "3":
            print("\n👋 Thanks for practicing! Keep improving!")
            break
            
        else:
            print("❌ Invalid choice. Please select 1-3.")


if __name__ == "__main__":
    main()
