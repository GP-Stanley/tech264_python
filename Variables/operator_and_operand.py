""" Understanding Operators and Operand"""

""" Math Operators

Operators	        Operation	             Example
    **	         Exponent	             2 ** 3 = 8
    %	         Modulus/Remainder    	 22 % 8 = 6
    //	         Integer division	     22 // 8 = 2
    /	         Division	             22 / 8 = 2.75
    *	         Multiplication	         3 * 3 = 9
    -	         Subtraction	         5 - 2 = 3
    +	         Addition	             2 + 2 = 4
"""




"""Operators"""
# Operators are symbols that tell the computer to perform specific tasks, like addition or comparison.
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Equality check ==

# a = 5
# b = 1

# print(a + b)              # addition
# print(a - b)              # subtraction
# print(a * b)              # multiplication
# print(a / b)              # division

"""Operands"""
# Operands are the values or data that operators act on.
# (for example) a, b


""" Comparison Operators

Operator	           Meaning
    ==	             Equal to
    !=	             Not equal to
    <	             Less than
    >	             Greater Than
    <=	             Less than or Equal to
    >=	             Greater than or Equal to
"""

# a = 5
# b = 1

# print(a == b)         # Output: False                  # Equal to
# print(a != b)         # Output: True                   # Not equal to
# print(a > b)          # Output: True                   # Greater than
# print(a < b)          # Output: False                  # Less than
# print(a >= b)         # Output: True                   # Greater than or equal to
# print(a <= b)         # Output: False                  # Less than or equal to

"""Logical operators = used on conditional statements"""

# and = checks two or more conditions if True
# or = checks if at least one condition is True
# not = True if condition is False, and vice versa

"""AND EXAMPLE"""

temp = -25

if temp > 0 and temp < 30:                  # checking if multiple conditions are True.
    print("The temperature is good.")
else:
    print("The temperature is bad.")


"""OR EXAMPLE"""

temp = 40

if temp <= 0 or temp >= 30:                  # checking if at least one condition is True.
    print("The temperature is bad.")
else:
    print("The temperature is good.")


"""NOT EXAMPLE"""

temp = 20
sunny = True                                # 'not' will change something from False to True and vice versa.

if temp <= 0 or temp >= 30:                 # checking if at least one condition is True.
    print("The temperature is bad.")
else:
    print("The temperature is good.")

if not sunny:                               # 'not' will change something from False to True and vice versa.
    print("It is cloudy outside.")
else:
    print("It is sunny outside.")
