#English explanation
#User input their current level which means a random number for now
#if level 100 or higer print You are worth becoming an Emperor of the Sea!
#if level is 50 or higer print Welcome to New World
#if level is 10 or higher print Welcome to grandline
#if level is under 10 print You got crushed by ocean waves

import random

level = int(input("Enter Your Level Honestly: "))
if level>=100:
    print("You are worth becoming an Emperor of the Sea")

elif level>=50:
    print("Welcome to New World")

elif level>=10:
    print("Welcome to GrandLine") 

else:
    bad_result = [
        "You got crushed by ocean waves",
        "You are now sinking to the bottom of the ocean",
        "A Sea King swallowed your whole ship",
        "Marines caught you",
        "Pirates Attacked you"
    ]

    random_death = random.choice(bad_result)

    print(random_death)

