#The Pseudocode (English Steps):
#
#Define a function called calculate_bounty that takes one ingredient inside its parentheses: (level).
#
#Inside the function (indented!):
#
#Create a variable called bounty_amount. Make it equal to level multiplied by 100,000.
#
#Use return bounty_amount to spit that number back out.
#
#Outside the function (not indented):
#
#Ask the user for their level using input() and convert it to an int.
#
#Create a variable called final_bounty and set it equal to calculate_bounty(your_input_variable).
#
#Print out the final bounty!

def calculate_bounty(level):
    bounty_amount = level * 100000
    return bounty_amount

a = int(input("Enter Your Level Honestly: "))
final_bounty = calculate_bounty(a)
print("Your Final Bounty is : ", final_bounty)
