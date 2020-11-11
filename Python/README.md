# Python README

Here's where all my Raspberry Pi Python code will be.

## Hello Python

For our first Python assignment, I created a program that simulates rolling a 6 or 20-sided die. 

```Python
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
	print roll
```

The process went fairly smoothly, with only one major hiccup: when I initially wrote the `while` loop, I named the variable which became `my_input` sipmly "input." However, `input` is already a function in Python, so it didn't recognize that I wanted it to be a variable. Once I changed it to `my_input`, the problem was solved.
