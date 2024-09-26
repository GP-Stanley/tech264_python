"""Use PyCharm/Python to the following subtasks:

Aim to have working code for each subtask
Document once you have it working - could be as simple as adding comments to each section of code
If you need to explain, research and document accordingly.

Here are the subtasks:

- Explain: What is a variable
- Explain: Why called a variable?

In your Python learning project, create a folder called 'variables', then create a new file called
'variables_examples.py' for the following tasks
- Set/assign a variable
- Try to set a variable with a number value
- Try to set a variable with a decimal value
- Try to set a variable with a string value
- How is using '==' different?

Explain: What's the difference between a dynamically typed language (like Python) and a strong typed language
Give an example of how they are different
- Print the data types of the variables you set values for above
- Overwrite the value of one of your variables which stores a number
- Check the id() of the variable before and after you overwrite the variable with a new number
- Why does the 'id' of the variable change?
- Ask the user for some input and print the input to the screen"""


"""What is a variable?"""

# variable = a resuable container for storing a value.
#            a variable behaves as if it were the value it contains.

# Why is it called a variable?
# because the value it holds can vary or change throughout the program's execution.

"""Why does the Id change?"""
# The id of a variable changes because a new object is created in memory when you
# assign a new value to the variable.


"""INTEGER"""
# a whole number.
                                                # How to check the datatype.
# age = 21                                      # print(type(age)) = <class 'int'>
# players = 2
# quantity = 5

# print(f"You are {age} years old")
# print(f"There are {players} players online")
# print(f"You would like to buy {quantity} items")

# -------------------------------------------------------------------

"""FLOATS"""
# a decimal number

# gpa = 3.2                                       # print(type(gpa)) = <class 'float'>
# distance = 2.5
# price = 10.99

# print(f"Your gpa is {gpa}")
# print(f"You ran {distance}km")
# print(f"The price is £{price}")

# ---------------------------------------------------------------------

"""STRINGS"""
# Strings are a series of characters: you can use 'single quotes' or "double quotes".

# name = "Bro"                                      # print(type(name)) = <class 'str'>
# food = "Pizza"

# print(f"Hello, {name}")
# print(f"You like {food}")


# -----------------------------------------------------------------------

"""How is using "==" different?"""
# The '==' operator checks if two values are equal.

# Example of using ==
# a = 5
# b = 5
# print(a == b)                                     # This will print True


# ------------------------------------------------------------------------

"""Difference between dynamically typed and strongly typed languages"""

"""Dynamically Typed"""
# In languages like Python, the 'type' of a variable is determined at runtime,
# and you can change the 'type' of a variable by assigning a new value to it.

# For example:

# x = 10                          # Dynamically Typed
# x = "Now I'm a string"

"""Strongly Typed"""
# In languages like Java, the 'type' of a variable is declared
# and cannot change. You must explicitly convert between types.

# y = 10                          # Strongly Typed
# print(y)                        # Output: 10

# y = "Now I'm a string!"
# print(y)                        # Output: Now I'm a string!


"""Id Function"""

# x = 42                                  # Initial assignment
# print(f"Initial id of x: {id(x)}")

# x = 99                                  # Overwrite with a new number
# print(f"New id of x: {id(x)}")

# How it works:
# The id() function checks the memory address of a variable before and after you overwrite it.
# The id changes after the reassignment because integers are immutable in Python,
# so a new object is created for the new value.
# It's not replacing the value, it created a new object and the id named that object.


"""User Input"""

# user_input = input("Enter something: ")
# print(f"You entered: {user_input}". How interesting!)




