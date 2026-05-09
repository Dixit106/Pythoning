#The English Pseudocode:
#
#Create a variable called secret_password and set it to a string (e.g., "omarchy").
#
#Create a variable called guess and set it to empty quotes: ""
#
#Start a while loop that runs as long as guess is not equal to (!=) the secret_password.
#
#Inside the loop: Ask the user for input() and save it into the guess variable.
#
#Outside the loop (at the very bottom): Print "Access Granted!" (Because if the code reaches this line, it means the while loop finally broke).

secret_password = "Omarchy"
guess = ""
while guess != secret_password:
    a = input("Guess the secret pass: ")

print("Access Granted")    