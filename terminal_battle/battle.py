#The english Psudocode
#1. Import your random module at the very top (for damage part)
#2. Create a dictionary called player. Give them a "Name", "Hp", "potions".
#3. Create a dictionary boss. Give them "name" and "hp"
#4. Print a dramatic battle into!
#5. Print the player's starting stats so they know what they have

import random

player = {"Name": input("Enter Your Name: "), "HP": 100, "Potions": 3}

boss = {"NameBoss": "Kai", "BossHP": 250}

print("A revenge hungary wild monster", boss["NameBoss"], "has appeared with", boss["BossHP"], "health!")

print("Player Stats: ", "\nName:", player["Name"], "\nHP:", player["HP"], "\nPotions:", player["Potions"])

