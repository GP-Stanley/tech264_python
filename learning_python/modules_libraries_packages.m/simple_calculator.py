from math_operations import*

# ^^ from <module> (a single file), import the functions.
# a library is a set of modules (files).
# a module is a single file imported.
# a package is installable. A module or a library can become a package if its installable.

# Mini-calculator

# first_num = int(input("Enter the first number: "))
# second_num = int(input("Enter the first number: "))
# result = add(first_num, second_num)

# print(f"{first_num} + {second_num} = {result}")

            # 'mo' mean module.
                                        # This part assigns the alias mo to the math_operations module.
                                        # With this name, you can call functions using the shorter name, like mo.add(5, 3).

# Testing the functions from math_operations module

# test_my_module.py
def test_add():
    return add(1, 2) == 3
    print(test_add())
