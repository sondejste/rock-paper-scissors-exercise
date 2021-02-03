# game
#print ("Rock, Paper, Scissors, Shoot!")
#^this was just a placeholder for setup


import random
#makes the random module and all of its parts accessible to us



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

foo = ['rock', 'paper', 'scissors']

computer_choice = random.choice(foo)

print(f"The computer chose: {computer_choice}")


print ("-------------------")

exit()


#determining who won

print ("Oh, the computer won. It's ok.")

print ("-------------------")

print ("Thanks for playing. Please play again!")