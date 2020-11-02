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

