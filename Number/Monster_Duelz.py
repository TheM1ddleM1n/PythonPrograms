import random

player_health = 100
monster_health = 100

print("🧙‍♂️ Welcome to Monster Duelz!")
while player_health > 0 and monster_health > 0:
    move = input("Choose your move player (attack/defend): ").lower()
    monster_move = random.choice(["attack", "defend"])

    if move == "attack" and monster_move != "defend":
        monster_health -= random.randint(10, 20)
        print("You hit the monster!")
    elif move == "defend":
        player_health += random.randint(5, 10)
        print("You brace yourself and you suddenly recover!")
    else:
        player_health -= random.randint(5, 15)
        print("The violent monster attacks you!")

    print(f"💖 Your Health: {player_health} | 👹 Monster Health: {monster_health}\n")

if player_health <= 0:
    print("☠️ Oh no! You were defeated!")
elif monster_health <= 0:
    print("🏆 You slayed the monster! Congrats!")

