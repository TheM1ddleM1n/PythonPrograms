import time
import random

print("🍷 Welcome to the Chateau of Food!")
print("It seems we are quite busy this evening...\n")

# Input validation
while True:
    try:
        money = int(input("💸 How much money did you slip the waiter? £"))
        break
    except ValueError:
        print("❌ That doesn't look like a number. Try again.")

# Add suspense.. with time.sleep!
print("\n🕰️ The waiter eyes you carefully...")
time.sleep(1.5)

# Decisions Decisions...
if money >= 50:
    print("💎 'Ah, Monsieur/Madame! Right this way to the VIP lounge.'")
    print("🪑 You are seated at a velvet booth with complimentary champagne.")
elif 20 <= money < 50:
    print("👌 'Hmm... generous. A table by the window just opened up.'")
    print("🍽️ You are seated with a view of the garden.")
elif 1 <= money < 20:
    print("🤏 'I suppose we can squeeze you in near the kitchen.'")
    print("🥘 You hear pots clanging and chefs shouting.")
else:
    print("😐 The waiter raises an eyebrow.")
    time.sleep(1)
    print("🧾 'Please, take a seat in the waiting area.'")
    time.sleep(1)
    print("🚪 A cold breeze blows in from the door as you're handed a buzzer.")
    time.sleep(1)
    print("📢 'Next!'")

# Random twist
if money >= 20:
    dessert = random.choice(["Crème brûlée", "Chocolate soufflé", "Lemon tart"])
    print(f"\n🍰 As a surprise, the chef sends out a complimentary {dessert}.")

print("\n🎭 Thank you for dining with us at the Chateau of Food! Please come again!")
