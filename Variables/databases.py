"""
Explain and demonstrate: Numeric data types: int and float
Explain and demonstrate: Boolean data type
Explain why the result is not 0.9999999... with this code and what lesson we should learn:
"""


"""Floating-Point Number"""
# A float is a number that has a decimal point.
# It can also be positive, negative, or zero.

# x = 10.5
# y = -5.75
# z = 0.0

# print(type(x))                    # Output: <class 'float'>
# print(type(y))                    # Output: <class 'float'>
# print(type(z))                    # Output: <class 'float'>


"""Boolean Data Type"""
# A Boolean data type can only have two values: True or False.
# It is used to represent the truth values of logic and Boolean algebra.
# False = 'empty', True has value.

# is_sunny = True
# is_raining = False

# print(type(is_sunny))             # Output: <class 'bool'>
# print(type(is_raining))           # Output: <class 'bool'>


"""Why the result is not..."""
# When you perform certain floating-point arithmetic operations in Python,
# you might not get the exact result you expect due to the way
# floating-point numbers are represented in computers. This is because floating-point numbers
# are stored in a binary format that can’t precisely represent some decimal numbers.

One_third = 1 / 3
print(One_third)                     # Python should show 0.3333333333333333
print(One_third * 3)                 # python rounds it to 1.0

# Explanation:
# The result is not exactly 0.3 because 0.1 and 0.2 cannot be precisely represented in binary.
# Instead, they are approximations, and when added together, the small errors accumulate,
# resulting in a tiny discrepancy.


"""Format Specifier: round"""
# format specifiers = {value:flags} format a value based on what flags are inserted.

# .(number)f = round to that many decimal places (fixed point)

price1 = 3.14159
price2 = -987.65
price3 = 12.34
                                                 # these flags will format our value a particular way depending
""".(number)f"""                                 # on what we insert after the colon.
# print(f"Price 1 is £{price1:.2f}")             # decimal precision (.2), floating point number (f).
# print(f"Price 2 is £{price2:.2f}")
# print(f"Price 3 is £{price3:.2f}")