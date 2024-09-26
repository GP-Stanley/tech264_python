"""
Explain: What is slicing strings?

Here is your starting code. You may need to:
- Write code to do what the comments ask for.
- Write a comment to explain what the code does.

Hw = "Hello world!"
print(Hw)

- Find out how many characters Hw has
- Get the character in the first position in Hw
- Get the last character
- Get the 2nd last character

- Write a comment to EXPLAIN what does this do: print(Hw[2:])
- Write a comment to EXPLAIN what does this do: print(Hw[-3:])
- Write a comment to EXPLAIN what does this do: print(Hw[:5])
- Starts from the second, stops at the fifth (doesn't include it)
"""

"""What is slicing strings?"""
# String slicing is a technique used to extract a portion of a string in programming.
# It allows you to create a new string from a subset of the original string by specifying a range of indices.
# This is particularly useful when you need to manipulate or analyse specific parts of a string.

# Find out how many characters 'Hw' has.
Hw = "Hello world!"
print(Hw)

length = len(Hw)                                            # How many characters there are.
print(f"{Hw} has {length} amount of characters.")


# Get the character in the first position in 'Hw'.
                                                            # What the first character is.
first_char = Hw[0]                                          # Characters start at '0'.
print(f"'{first_char}' is the first character in {Hw}.")


# Get the last character in 'Hw'.
last_char = Hw[-1]                                          # What the last character is.
print(f"The last character is: '{last_char}'.")              # Output: !


# Get the second to last character.
second_last_char = Hw[-2]                                               # Second to last character.
print(f"The second-to-last character is: '{second_last_char}'.")        # Output: d


# Write a comment to EXPLAIN what this does: print(Hw[2:])
print(Hw[2:])                                # This slices the string from the 3rd character to the end.
                                             # Output: "llo world!"


# Write a comment to EXPLAIN what this does: print(Hw[-3:])
print(Hw[-3:])                              # This slices the string from the 3rd last character to the end.
                                            # Output: "ld!"


# Write a comment to EXPLAIN what does this do: print(Hw[:5])
print(Hw[:5])                       # This slices the string from the beginning to the 5th character (exclusive).
                                    # Output: "Hello"


# Starts from the second, stops at the fifth (doesn't include it)
slice_example = Hw[1:5]         # This slices the string from the 2nd character to the 5th character (exclusive).
print(slice_example)            # Output: "ello"
