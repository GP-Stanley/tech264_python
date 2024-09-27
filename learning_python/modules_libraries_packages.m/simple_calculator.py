from math_operations import *
# ^^ from <module> (a single file), import the functions.
# a library is a set of modules (files).
# a module is a single file imported.
# a package is installable. A module or a library can become a package if its installable.

# Mini-calculator

# first_num = int(input("Enter the first number: "))
# second_num = int(input("Enter the first number: "))
# result = add(first_num, second_num)

# print(f"{first_num} + {second_num} = {result}")

import math_operations as mo            # 'mo' mean module.
                                        # This part assigns the alias mo to the math_operations module.
                                        # With this name, you can call functions using the shorter name, like mo.add(5, 3).

# Testing the functions from math_operations module
print("Addition of 5 and 3:", mo.add(5, 3))         # Output: 8
print("Subtraction of 5 and 3:", mo.subtract(5, 3)) # Output: 2
print("Multiplication of 5 and 3:", mo.multiply(5, 3)) # Output: 15
print("Division of 5 by 3:", mo.divide(5, 3))       # Output: 1.6666666666666667
print("Exponentiation of 2 to the power of 3:", mo.exponentiate(2, 3))  # Output: 8
print("Evaluation of expression '2 + (3 - 1) * 5':", mo.evaluate_expression("2+(3-1)*5"))  # Output: 12
