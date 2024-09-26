from math_operations import *
# ^^ from <module> (a single file), import the functions.
# a library is a set of modules (files).
# a module is a single file imported.
# a package is installable. A module or a library can become a package if its installable. 

# Mini-calculator

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = add(first_num, second_num)

print(f"{first_num} + {second_num} = {result}")