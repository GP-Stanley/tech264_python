"""Do what is written in the comments.

Starting code:

int_string = "6"

# convert int_string to an integer
# after converting, print its data type to the screen
# convert int_string to float
# after converting, print its data type to the screen

"""

int_string = "6"

# convert int_string to an integer
int_value = int(int_string)                   # 'int(int_string)' converts the string into an integer.
print(int_value)                              # Output: 6

# print its data type to the screen
print(type(int_value))                        # type() prints the data type. Output: <class 'int'>

# convert int_string to float
int_value = float(int_string)                   # 'float(int_string)' converts the string into a float.
print(int_value)                                # Output: 6.0

# print its data type
print(type(int_value))                          # Output: <class 'float'>
