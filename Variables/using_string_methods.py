"""Trim spaces off the beginning and end of a string:

Starting code:
str_with_extra_spaces = "   extra spaces at the start and end   "

- Write comment to explain what this does: print(len(str_with_extra_spaces))
- Write comment to explain what this does: print(len(str_with_extra_spaces.INSERT_CORRECT_METHOD_HERE()))

```
Next, use this new starting code for the next set of subtasks. Write code to do what the comments ask for.
```
example_text = "here's some text with some words of text"
- count how many times the substring 'text' occurs within example_text & print it to the screen
- convert example_text to lowercase & print it to the screen
- convert example_text to uppercase & print it to the screen
- capitalise the first letter in example_text & print it to the screen
- replace the word 'with' in example_text with a comma (,) instead & print it to the screen
"""

"""Task 1"""

str_with_extra_spaces = "   extra spaces at the start and end   "

# Write comment to explain what this does:
print(len(str_with_extra_spaces))
# Output: 39
# This shows how many characters are in the string, including the spaces at the beginning and end.

# Write comment to explain what this does
print(len(str_with_extra_spaces.strip()))
# Output: 33
# This shows how many characters are in the string after removing the spaces at the beginning and end.
# Use the .strip() method.


"""Task 2"""
example_text = "here's some text with some words of text"

# Count how many times the substring 'text' occurs within example_text & print it to the screen
text_count = example_text.count('text')
print(f"The word 'text' appears {text_count} times.")                      # Output: 2

# Convert example_text to lowercase & print it to the screen
lowercase_text = example_text.lower()
print(f"This is it in lowercase: {lowercase_text}.")                       # Output: "here's some text with some words of text"

# Convert example_text to uppercase & print it to the screen
uppercase_text = example_text.upper()
print(f"This is it in uppercase: {uppercase_text}.")                       # Output: "HERE'S SOME TEXT WITH SOME WORDS OF TEXT"

# Capitalise the first letter in example_text & print it to the screen
capitalized_text = example_text.capitalize()
print(f"This has capitalised the first letter: {capitalized_text}/")       # Output: "Here's some text with some words of text"

# Replace the word 'with' in example_text with a comma (,) instead & print it to the screen
replaced_text = example_text.replace(' with', ',')
print(f"We've replaced 'with' with a comma: {replaced_text}.")              # Output: "here's some text , some words of text"



