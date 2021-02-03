# game
#print ("Rock, Paper, Scissors, Shoot!")
#^this was just a placeholder for setup


import random
#makes the random module and all of its parts accessible to us
#could also only import the function we need from the random module, in this case "random.choice"


#add user input for username/name

print ("-------------------")
print ("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print ("-------------------")

#
#asking user for input
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

print (f"You chose: {user_choice}")

#ways to format:
#just printing: print("You chose:", user_choice)
#string concatonation: print("You chose:" + user_choice)
#string interpolation: print(f"You chose: {user_choice})


#simulating computer input

print ("-------------------")


#need to validatue user selection
#stop the program (prior to determining winner) and if the user choice is invalid, end the program


options = ["rock", "paper", "scissors"]

user_choice.lower()

if user_choice in options:
    print("Great Choice!")
else:
    print("Sorry, you need to choose an option from the list and try again.")
    exit()


computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")


print ("-------------------")
#determining who won
if computer_choice == user_choice: 
        print("It's a tie!")
    #double "==" is used because a single "=" is used to set variables equal to values. The double "==" needs to be used for equality operations/checking (think "is whats on the left, the same as whats on the right?")

#the elif function is the same as elseif in other programs. This method is one of several correct options. Others include nested if statements.
elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Congrats")
elif user_choice == "paper" and computer_choice == "scissors":
        print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "paper":
        print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "rock":
        print("Oh! The computer won, that's ok!")

    #the "and" operator creates contingencies


print ("-------------------")

print ("Thanks for playing. Please play again!")