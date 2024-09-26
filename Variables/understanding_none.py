"""
- What is None in Python?
- When is it commonly used?
- What's the equivalent in some other programming languages?

Most important: What happens when you convert None to a boolean?

- Write a piece of Python code to prove it
- Write a piece of Python code to...

1. assign x to be None
2. print whether my variable x is equal to None"""


"""What is None in Python?"""
# The None keyword is used to define a null value, or no value at all.
# None is not the same as 0, False, or an empty string.
# None is a data type of its own (NoneType) and only None can be None.

# x = None
# print(x)                      # Outcome: None


# if x:
#  print("Do you think None is True?")
# elif x is False:
#   print ("Do you think None is False?")
# else:
#  print("None is not True, or False, None is just None...")        # Output: "None is not True, or False, None is just None..."

# print(type(None))             # Output: <class 'NoneType'>


"""When is none commonly used?"""
# 1. Default value for arguments. This allows the function to check if
#    an argument was provided by the user.

# 2. Initialising variables that will later be assigned a value.
#    This is useful for setting up variables that might not have an initial value.

# 3. In data structures like dictionaries, 'None' can indicate missing
#    or default values.

# 4. Functions that do not explicitly return a value will return 'None'
#    by default. This is also used to indicate that a function has no meaningful
#    return value.

# 5. When working with optional parameters, 'None' can be used to signify
#    that the parameter is optional and has not been provoked.

# 6. 'None' can act as a sentinel value in algorithms to indicate the end
#    of a list or the absense of a value.


"""What's the equivalent in some other programming languages?"""
# JavaScript: null (represents the intentional absence of any object value.
#             undefined (indicates that a variable has been declared but not yet assigned a value)

# C#: null (it indicates that a reference does not point to any object).
# C++: nullptr (used to represent a null pointer).
# Ruby: nil (represents the absence of a value or an undefined value).
# Go: nil (used to represent zero values for pointers, interfaces, maps, slices, channels, and function types.


"""What happens when you convert None to a boolean?"""
# When you convert None to a boolean in Python, it evaluates to False. This is because
# None is considered a “falsy” value in Python.

# Example

x = None                            # Step 1: Assign x to be None

if x is None:                       # Step 2: Print whether my variable x is equal to None
    print("x is None")              # This will be printed
else:
    print("x is not None")          # Outcome: "x is None"

print(bool(x))                      # Additional: Convert None to a boolean and print the result
                                    # Output: False

# there are way to check for None:
# if X is None                          (don't use "==")
# if yes returns True