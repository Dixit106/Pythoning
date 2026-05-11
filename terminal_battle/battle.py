#The english Psudocode 01
#1. Import your random module at the very top (for damage part)
#2. Create a dictionary called player. Give them a "Name", "Hp", "potions".
#3. Create a dictionary boss. Give them "name" and "hp"
#4. Print a dramatic battle into!
#5. Print the player's starting stats so they know what they have

import random
import time 


player = {"Name": input("Enter Your Name: "), "HP": 100, "Potions": 3}

boss = {"NameBoss": "Kai", "BossHP": 200}

print("A revenge hungary wild monster", boss["NameBoss"], "has appeared with", boss["BossHP"], "health!")
time.sleep(1.5)
print("Player Stats: ", "\nName:", player["Name"], "\nHP:", player["HP"], "\nPotions:", player["Potions"])
time.sleep(1.5)
while True:
    print("--- NEW TURN ---")
    action = input("Attack OR Heal: ").lower()

    if action == "attack":
        player_dmg = random.randint(15,40)
        boss["BossHP"] = boss["BossHP"] - player_dmg
        print("You hit", boss["NameBoss"], "with", player_dmg,"damage!")
        time.sleep(1.5)
    elif action == "heal":
        if player["Potions"] > 0:
            player["HP"] = player["HP"] + 30
            player["Potions"] = player["Potions"] - 1
            print("You healed, +30 HP!")
            time.sleep(1)
            print("Potions left: ", player["Potions"])
            time.sleep(1)
    else:
        print("Umm, That's not possible")
        time.sleep(1)

    if boss["BossHP"] > 0:
        boss_dmg = random.randint(10,25)
        player["HP"] = player["HP"] - boss_dmg
        print("The boss only attacks and deals", boss_dmg, "damage!")
        time.sleep(1)

    print("Player Stats NEW: ", "\nName:", player["Name"], "\nHP:", player["HP"], "\nPotions", player["Potions"])
    time.sleep(1)
    print("Boss Stats NEW: ", "\nName:", boss["NameBoss"], "\nHP:", boss["BossHP"])
    time.sleep(1)

    if boss["BossHP"] <= 0:
        print("You defeated the monster! Your Adventure Continues")
        time.sleep(1)
        break

    elif player["HP"] <= 0:
        print("You Died, Game Over")
        time.sleep(1)
        break