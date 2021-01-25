# Automatic Dice Roller
# Written by Rowan Miller

from random import randint

global roll # creates a variable for the result of the roll to be stored in

print("Automatic Dice Roller")

print("Press Enter to roll a d6. Type d20, then Enter to roll a d20. Press x, then Enter to quit.")

while 1 == 1:
	my_input = input() # asks the user for input
	if my_input == "x":
		break # stops the loop if the user enters x
	elif my_input == "d20":
		roll = randint(1,20) # takes a random number between 1 & 20 and saves it as the result of the roll.
	else:
		roll = randint(1,6) # takes a random number between 1 & 6 and saves it as the result of the roll.
	print(roll) # outputs the result of the roll.

