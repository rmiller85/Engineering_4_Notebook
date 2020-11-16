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

## Calculator

My next task was to write a program that takes two numbers and outputs their sum, difference, product, quotient, and modulo (remainder). Additionally, I was given what should roughly be the last 5 lines of my code:

```Python
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
```

These lines told me that I needed to create a function called `doMath` that took 3 arguments. I inferred that the first two arguments were the numbers that the user inputs and the third told the function which operation to do on the numbers. Of course, I first needed to establish what those two numbers were. I did so with the use of an `input` function, as shown below.

```Python
print("Enter 2 numbers. The sum, difference, product, quotient, and modulo of the two numbers will be calculated.")

Num1 = input("Type your first number here:")
Num2 = input("Type your second number here:")
```

Oh yeah, I also renamed the variables for the numbers `Num1` and `Num2` because it made more sense to me. Now, I had my numbers. I just needed to use them in the `doMath` function. Here's the simplified version of what `doMath` looked like:

```Python
def doMath(a,b,c)
	if c == 1:
		add the numbers, return the result
	elif c == 2:
		subtract them
	elif c == 3:
		multiply
	elif c == 4:
		divide
	elif c == 5:
		find modulo
```

For addition, subtraction, multiplication, and the modulo, this was a simple process: just apply the proper command to the numbers and return the result. The addition would look like this:

```Python
if c == 1:
        return str(int(a) + int(b))
```

If it were subtraction, the plus sign would be replaced with a minus. If multiplication, an asterisk. If modulo, a percent symbol. Simple as that. Division was a little more tricky. I needed to round to two decimal places. Thankfully, there's a command just for that: `round(input,decimal places)` I could have likely done this with just one line if I layered a bunch of parentheses, but I'm a sloppy coder and it was easier to just do it in two steps. First, store the result of dividing the numbers in variable `d`. Then, return the result of `round(d,2)`. Here's the full excerpt.

```Python
elif c == 4:
	d = (int(a) / int(b))
	return str(round(d,2))
```

Finally, `doMath` was complete. Here's the finished product, all put together.

```Python
# Python Calculator
# Written by Rowan Miller

print("Enter 2 numbers. The sum, difference, product, quotient, and modulo of the two numbers will be calculated.")

Num1 = input("Type your first number here:") # stores the user's chosen numbers in variables to be used later
Num2 = input("Type your second number here:")

def doMath(a,b,c): # runs some mathematical equations using the two numbers given by the user. The equation that is run is determined by c.
    if c == 1:
        return str(int(a) + int(b)) # adds the two numbers that the user inputs. Before adding them, they are converted into integers.
    elif c == 2:
        return str(int(a) - int(b)) #subtracts them
    elif c == 3:
        return str(int(a) * int(b)) #multiplies
    elif c == 4:
        d = (int(a) / int(b)) # divides the user inputs and stores them in the variable d. This is done instead of simply returning the result because the number needs to be rounded.
        return str(round(d,2)) # rounds the result to 2 decimal places and returns it as a string.
    elif c == 5:
        return str(int(a) % int(b)) # solves for the remainder.

print("Sum:\t\t" + doMath(Num1,Num2,1)) # inputs the user's numbers into doMath and, since c==1, adds them together.
print("Difference:\t" + doMath(Num1,Num2,2)) # the same, but subtraction, since c==2.
print("Product:\t" + doMath(Num1,Num2,3)) # multiplies
print("Quotient:\t" + doMath(Num1,Num2,4)) # divides
print("Modulo:\t\t" + doMath(Num1,Num2,5)) # finds modulo
```

Lessons learned: Integers don't have decimals! A modulo is the remainder of two numbers that are divided. I learned that `/t` creates a large blank space in a line. Also, I looked at Vann's code once or twice to help me through some blocks. [Here's his Github.](https://github.com/vwellmo57)
