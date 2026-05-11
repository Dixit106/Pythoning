#The english Psudocode 01
#1. Import your random module at the very top (for damage part)
#2. Create a dictionary called player. Give them a "Name", "Hp", "potions".
#3. Create a dictionary boss. Give them "name" and "hp"
#4. Print a dramatic battle into!
#5. Print the player's starting stats so they know what they have

import random
import time 
import sys

def slow_print(text):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(0.04)
    print()



player = {"Name": input("Enter Your Name: "), "HP": 100, "Potions": 3}

boss = {"NameBoss": "Kai", "BossHP": 200}

slow_print(f"A revenge hungary wild monster {boss['NameBoss']} has appeared with {boss['BossHP']} health!")
time.sleep(1.5)
slow_print(f"Player Stats:  \nName: {player['Name']} \nHP: {player['HP']} \nPotions: {player['Potions']}")
time.sleep(1.5)
while True:
    slow_print(f"--- NEW TURN ---")
    action = input("Attack OR Heal: ").lower()

    if action == "attack":
        player_dmg = random.randint(15,40)
        boss["BossHP"] = boss["BossHP"] - player_dmg
        slow_print(f"You hit {boss['NameBoss']} with {player_dmg} damage!")
        time.sleep(1.5)
    elif action == "heal":
        if player["Potions"] > 0:
            player["HP"] = player["HP"] + 30
            player["Potions"] = player["Potions"] - 1
            slow_print(f"You healed +30 HP!")
            time.sleep(1)
            slow_print(f"Potions left:  {player['Potions']}")
            time.sleep(1)
    else:
        slow_print(f"Umm... That's not possible")
        time.sleep(1)

    if boss["BossHP"] > 0:
        boss_dmg = random.randint(10,25)
        player["HP"] = player["HP"] - boss_dmg
        slow_print(f"The boss only attacks and deals {boss_dmg} damage!")
        time.sleep(1)

    slow_print(f"Player Stats NEW:  \nName: {player['Name']} \nHP: {player['HP']} \nPotions {player['Potions']}")
    time.sleep(1)
    slow_print(f"Boss Stats NEW:  \nName: {boss['NameBoss']} \nHP: {boss['BossHP']}")
    time.sleep(1)

    if boss["BossHP"] <= 0:
        slow_print(f"You defeated the monster! Your Adventure Continues")
        time.sleep(1)
        break

    elif player["HP"] <= 0:
        slow_print(f"You Died... Game Over...")
        time.sleep(1)
        break