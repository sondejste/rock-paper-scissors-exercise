# game

import random
#makes the random module and all of its parts accessible to us
#could also only import the function we need from the random module, in this case "random.choice"


from dotenv import load_dotenv

import os

#creating a username
load_dotenv()

username = os.getenv(username, default="Player One") 
print(f"Welcome {username}")

exit()


#beginning gameplay

#print ("-------------------")
#print ("Welcome 'Player One' to my Rock-Paper-Scissors game...")
#print ("-------------------")

#asking user for input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

#user_choice.lower() makes the string all lowercase

print (f"You chose: {user_choice.lower()}")

#ways to format:
#just printing: print("You chose:", user_choice)
#string concatonation: print("You chose:" + user_choice)
#string interpolation: print(f"You chose: {user_choice})

print ("-------------------")

#need to validate user selection
#stop the program (prior to determining winner) and if the user choice is invalid, end the program


options = ["rock", "paper", "scissors"]

if user_choice.lower() in options:
    print("Great Choice!")
else:
    print("Sorry, you need to choose an option from the list and try again.")
    exit()

print ("-------------------")


#simulating computer input

computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")

print ("-------------------")

#determining a winner

if computer_choice == user_choice.lower(): 
        print("It's a tie!")
    #double "==" is used because a single "=" is used to set variables equal to values. The double "==" needs to be used for equality operations/checking (think "is whats on the left, the same as whats on the right?")

#the elif function is the same as elseif in other programs. This method is one of several correct options. Others include nested if statements.

#this section has been adapted from Will Perrone's solution shared in Slack

elif user_choice.lower() == "paper" and computer_choice == "rock":
        print("You win! Congrats!")
elif user_choice.lower() == "paper" and computer_choice == "scissors":
        print("Oh! The computer won, that's ok!")
elif user_choice.lower() == "rock" and computer_choice == "paper":
        print("Oh! The computer won, that's ok!")
elif user_choice.lower() == "rock" and computer_choice == "scissors":
        print("You win! Congrats!")
elif user_choice.lower() == "scissors" and computer_choice == "paper":
        print("You win! Congrats!")
elif user_choice.lower() == "scissors" and computer_choice == "rock":
        print("Oh! The computer won, that's ok!")

    #the "and" operator creates contingencies


print ("-------------------")

print ("Thanks for playing. Please play again!")