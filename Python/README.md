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

## Quadratic Solver

Oh how I would've killed for this in 9th grade. I created a program where, upon inputing coefficients, the user is given the real roots of a quadratic equation. The basis of this program was simple: the user inputs coefficients. These coefficients are run through a function that replicates the quadratic formula. The results are then returned and printed. However, there was one small wrench in the gears. The assignment required that the roots were put into an `array` and this array would be printed. Here's my finished code.

```Python
# Quadratic Solver
# Written by Rowan Miller

from math import sqrt # allows me to take a square root
from numpy import array # allows me to make arrays

print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0.")

# sets the values for the equation according to user input
a = input("a = ")
b = input("b = ")
c = input("c = ")

def QuadSolver(a,b,c):
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    disc = (b**2) - (4*a*c)
    
    if disc < 0:
        print("No real roots exist.") # if the discriminant was less than zero, it would require taking the square root of a negative number, which breaks the function.
    
    root1 = ((b*-1) - sqrt(disc)) / (2*a) # runs the quadratic formula where the plus/minus is a minus
    root2 = ((b*-1) + sqrt(disc)) / (2*a) # runs it with plus
    
    my_array = [root1,root2]
    
    return(my_array)
    
returned_array = QuadSolver(a,b,c) # since my_array was returned from QuadSolver, returned_array is defined as my_array

print(returned_array) # prints the roots that have been returned from the function
```

Before doing this assignment, I didn't even know what an `array` was! *edit: it turns out I still didn't. Now I know that I had been using a `list` the whole time.* An ~~`array`~~ `list` is a collection of values stored together. Stored together like this, they can be manipulated as a group; for example, if they all were `int`s, a user could add one to every value in the ~~`array`~~ `list`. Alternatively (and more relevantly), values such as `root1` or `root2` can be stored inside a `list`, then printed together with `print(my_array)`.

## Strings and Loops

To demonstrate my understanding of lists, loops, and strings, I has to create a program where upon receiving a sentence from a user, the program returns each individual letter separately, with a hyphen accounting for spaces. It sounded fairly simple: just use the `split()` function. Of course, it's never that simple.

```Python
sent_original = input("Type a simple sentence and press enter.")
sent_words = sent_original.split()
final_list = []
```

First, the user's sentence is taken and stored in `sent_original`. Then, the string of the full sentence is broken into a list (called `sent_words`) of strings for each individual word. Finally, an empty list, `final_list`, is created. It's a surprise tool that will help us later. Next, splitting the words into characters.

```Python
for word in sent_words:
  word += "-"
  split_letters = list(word)
  for letter in split_letters:
    final_list.append(letter)
```

Now, the strings inside `sent_words` are processed through a `for` loop one at a time. First, a hyphen is added onto the end of each string. This would turn the string `"Hello"` into `"Hello-"`. This way, when `"Hello"` is split into individual characters, it becomes `['H','e','l','l','o','-']`, providing the space at the end of the word. Then, *another* list is created: `split_letters`. It is the list of all the characters in whichever word is currently being processed through the `for` loop. Also, turns out that `split()` doesn't do quite what I initially thought. It splits a string with multiple words into a list of strings. However, to split a string of one word into a list of characters, I needed the `list()` function. So now, `split_letters` has been defined as a list of the characters that make up a word in `sent_words`. Finally, I can add this list of letters to `final_list`! I do this by looping through each index in `split_letters` and `append`ing them to `final_list`. Each time the function loops, the same process is done on each new word, so `split_letters` gets a new value and new things are `append`ed to `final_list`.

```Python
for thing in final_list:
  print(thing)
```

Finally, after the sentence has been broken into words, each word has been broken into letters, and they've all been added to `final_list`, the list is ready to be printed. A `for` loop cycles through `final_list`, printing out each value one after another. Here's the full, commented code:

```Python
sent_original = input("Type a simple sentence and press enter.")
sent_words = sent_original.split() # splits
final_list = [] # creates the final list that each letter will go into

for word in sent_words: # cycles through each word in the list of words
  word += "-" # adds a hyphen to the end of each word
  split_letters = list(word) # splits each word into a list of letters
  for letter in split_letters: # cycles through each letter in each list of letters
    final_list.append(letter) # adds each letter to the final list

for thing in final_list:
  print(thing) # prints everything that has been put into the final list
```
