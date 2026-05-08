#Import your random module at the top.
#
#Create a list called chest with at least 4 items in it (e.g., "Dragon Scale", "Rusty Dagger").
#
#Create a variable called total_gold and set it to 0. (You need a place to store your money!).
#
#Start your for loop: for loot in chest:
#
#Inside the loop (indented):
#
#Generate a random number between 10 and 1000 for the item_value.
#
#Print out the item's name and its value (e.g., "Dragon Scale is worth 500 gold.")
#
#Add that item_value to your total_gold. (Hint: total_gold = total_gold + item_value).
#
#Outside the loop (not indented, at the very bottom):
#
#Print the final total_gold.

import random

chest = ["Dragon Scale", "Rusty Dagger", "Diamond Sword", "Unknown Matterial", "Shiny Gem"]
total_gold = 0

for loot in chest:
    item_value = random.randint(10,100)
    print(loot, "is worth", item_value, "gold")
    total_gold = item_value + total_gold

print("total_gold = ", total_gold)

