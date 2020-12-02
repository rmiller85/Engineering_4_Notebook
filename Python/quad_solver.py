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
