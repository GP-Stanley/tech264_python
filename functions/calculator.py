from math_operations2 import *

"""complete a viable basic calculator using functions.
MVP (each of these should be in a separate function):
* Can add 2 numbers
* Can subtract 2 numbers
* Can multiply 2 numbers
* Can divide 2 numbers
 """

# Function to add two numbers.
def add(a, b):
    return a + b

# Function to subtract two numbers.
def subtract(a, b):
    return a - b

# Function to multiply two numbers.
def multiply(a, b):
    return a * b

# Function to divide two numbers.
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."


print("Addition of 8 and 4:", add(8, 4))
print("Subtraction of 8 and 4:", subtract(8, 4))
print("Multiplication of 8 and 4:", multiply(8, 4))
print("Division of 8 by 4:", divide(8, 4))
print("Division of 8 by 0:", divide(8, 0))

print("------------------------------------------------------------------------------")
"""Taking it to the next level: 
* Implement more complex operations, such as handling parentheses, exponentiation 
* More advanced operations should continue to be broken into separate functions 
"""

# Constant Expressions
x = 15 + 1.3

print(x)

print("------------------------------------------------------------------------------")

# Relational Expressions
a = 21
b = 13
c = 40
d = 37

p = (a + b) >= (c - d)
print(p)

print("------------------------------------------------------------------------------")

P = (10 == 9)
Q = (7 > 5)

# Logical Expressions
R = P and Q
S = P or Q
T = not P

print(R)
print(S)
print(T)

print("------------------------------------------------------------------------------")

# Bitwise Expressions
a = 12

x = a >> 2
y = a << 1

print(x, y)

print("------------------------------------------------------------------------------")

# Combinational Expressions
a = 16
b = 12

c = a + (b >> 1)
print(c)

print("------------------------------------------------------------------------------")

