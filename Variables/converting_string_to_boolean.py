"""Answer these questions:

When does a string convert to False?
When does a string convert to True?
Write a piece of Python code to prove your answers.

"""
# BOOLEAN, bool()

# online = True                         # Displaying it like this is typically uncommon.
# for_sale = False                      # It is normally used in an if, else statement.
# running = True

# print(f"Are you online?: {online}")                       # Output: True.
# print(f"Is this item for sale?: {for_sale}")              # Output: False.
# print(f"Game running: {running}")                         # Output: True.

"""When does a string convert to False?"""
# If the value of both operands is the same, the comparison operator returns true. Otherwise, it returns false.
# To convert a string to a boolean with the help of the comparison operator, we need to create
# a string that contains "true". Then, we need to compare this string with the given string.

empty_string = ""                               # Example of an empty string
boolean_value = bool(empty_string)              # Convert the empty string to a boolean
print(boolean_value)                            # Output: False

# In this example:
# empty_string is an empty string ("").
# When we use the bool() function to convert empty_string to a boolean, it returns False because the string is empty.


"""When does a string convert to True?"""
# A string converts to True when it is non-empty. This means that any string containing
# one or more characters, including spaces, will be evaluated as True.

non_empty_string1 = "Hello"                         # Examples of strings that convert to True
non_empty_string2 = " "
non_empty_string3 = "False"

print(bool(non_empty_string1))                      # Output: True
print(bool(non_empty_string2))                      # Output: True
print(bool(non_empty_string3))                      # Output: True


