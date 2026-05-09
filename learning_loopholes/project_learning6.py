#The Pseudocode:
#
#Start an infinite while True: loop.
#
#Inside the loop, put a try: block.
#
#Ask the user to input a 4-digit PIN, and convert it to an int().
#
#If it works, print "PIN Accepted" and use the break command to smash out of the infinite loop.
#
#Put an except ValueError: block right under the try block.
#
#If they typed letters instead of numbers, print "System failure: Numbers only! Try again." (The loop will then automatically restart).

while True:

    try:
        pin = int(input("ENTER 4-digit PIN: "))
        print("PIN Accepted!")
        break 

    except ValueError:
        print("System failure: Something went wrong! The loop is restarting...")

print("Welcome to the secret vault")
