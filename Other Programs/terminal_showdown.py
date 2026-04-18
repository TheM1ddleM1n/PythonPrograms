import random
import time

# 🎮 Game Setup
score = 0
streak = 0
questions_answered = 0


# 🖥️ Loading Screen
def loading_screen():
    print("🔄 Booting Terminal Showdown", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n✅ Ready!\n")
    time.sleep(1)


# 🧠 Question Bank
question_bank = {
    "Science": [
        {"q": "What planet is known as the Red Planet?", "a": "mars"},
        {"q": "What gas do plants absorb from the atmosphere?", "a": "carbon dioxide"},
        {"q": "What is the chemical symbol for gold?", "a": "au"},
    ],
    "History": [
        {
            "q": "Who was the first President of the United States?",
            "a": "george washington",
        },
        {"q": "In which year did World War II end?", "a": "1945"},
        {"q": "What wall fell in 1989?", "a": "berlin wall"},
    ],
    "Memes": [
        {"q": "Finish the phrase: 'One does not simply...'", "a": "walk into mordor"},
        {"q": "What animal is known for 'Dramatic Chipmunk'?", "a": "prairie dog"},
        {"q": "What is the name of the Shrek swamp song?", "a": "all star"},
    ],
}

# 👑 Final Boss Question
final_boss = {
    "q": "You're in a room with two doors. One leads to freedom, the other to doom. Two guards stand watch: one always lies, one always tells the truth. You can ask one question. What do you ask?",
    "a": "what would the other guard say",
}


# ⏱️ Timed Question
def ask_question(q_obj, is_boss=False):
    global score, streak, questions_answered

    print("\n⏳ Get ready for your question!")
    for i in range(3, 0, -1):
        print(f"{i}...", end=" ", flush=True)
        time.sleep(1)
    print("GO!\n")
    time.sleep(0.3)

    print(f"🧠 Question: {q_obj['q']}")
    start = time.time()
    answer = input("Your answer: ").strip().lower()
    end = time.time()
    elapsed = round(end - start, 2)

    correct = q_obj["a"]
    if answer == correct:
        base_points = 10
        bonus = streak * 2
        time_bonus = max(0, int(5 - elapsed))
        total = base_points + bonus + time_bonus
        if is_boss:
            total *= 2
            print("👑 FINAL BOSS DEFEATED! DOUBLE POINTS!")
        score += total
        streak += 1
        print(f"✅ Correct! +{total} points (Streak: {streak})")
    else:
        print(f"❌ Wrong! The correct answer was: '{correct.title()}'")
        streak = 0
    questions_answered += 1


# 📚 Category Selection
def choose_category():
    print("\n📚 Choose a category:")
    for i, cat in enumerate(question_bank.keys(), 1):
        print(f"{i}. {cat}")
    choice = input("Enter number: ")
    categories = list(question_bank.keys())
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        return categories[int(choice) - 1]
    else:
        print("❌ Invalid choice. Defaulting to 'Science'.")
        return "Science"


# 🎉 Endgame Summary
def show_results():
    print("\n🎊 QUIZ COMPLETE!")
    print(f"Questions Answered: {questions_answered}")
    print(f"Final Score: {score}")
    if score >= 80:
        print("👑 You conquered the quiz realm!")
    elif score >= 50:
        print("🏆 You're a certified brainiac!")
    elif score >= 30:
        print("👏 Solid effort, quiz warrior.")
    else:
        print("🧃 You need more juice. Try again!")


# 🏁 Game Loop
def play_quiz():
    print("""
  ____        _       _     _             
 |  _ \\ _   _| |_ ___| |__ (_)_ __   __ _ 
 | |_) | | | | __/ __| '_ \\| | '_ \\ / _` |
 |  __/| |_| | || (__| | | | | | | | (_| |
 |_|    \\__,_|\\__\\___|_| |_|_|_| |_|\\__, |
                                    |___/ 
    """)
    loading_screen()
    print("Welcome to Terminal Showdown! Created by TheM1ddleM1n")
    rounds = 5
    for _ in range(rounds):
        category = choose_category()
        question = random.choice(question_bank[category])
        ask_question(question)

    # ⚔️ Final Boss Round
    print("\n⚔️ FINAL BOSS! ⚔️")
    ask_question(final_boss, is_boss=True)

    show_results()


# Load game
play_quiz()
