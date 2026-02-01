# 🎂 Age Eligibility Checker

try:
    age = int(input("🔍 What is your age? "))

    if age >= 16:
        print("\n🎉 Congrats! You're old enough to participate.")
    else:
        print("\n🚫 Sorry, you're too young. Come back when you're 16 or older!")

except ValueError:
    print("\n⚠️ Please enter a valid number for your age.")

input("\n👋 Press Enter to exit.")
