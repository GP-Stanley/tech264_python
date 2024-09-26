"""Starting code:

bad_string = 'I said 'Wow!''
print(bad_string)

Explain: Why does this fail?
- Find 3 ways to make this string assignment work
Condition: The Wow! must be surrounded in quotes when it prints to the screen
Explain: What is best practice when deciding what quotes to use around strings in Python?
# this is a matter of what your teams prefer.
"""

"""Why does the starting code fail?"""
# Because it uses single quotes to close the string and also within the string ('Wow!').
# \ (escaping a character), it allows you to introduce a special character.
# used to understand that it can treat other characters

# Using double quotes and single quotes inside the string.
bad_string = "I said 'Wow!'"
print(bad_string)                                   # Output: I said 'Wow!'

# the backslash separates the single quotes from the string itself.
bad_string = "I said \'Wow!\'"
print(bad_string)                                   # Output: I said 'Wow!'

bad_string = 'I said \'Wow!\''
print(bad_string)

# separated quotes.
bad_string = 'I said \"Wow!\"'
print(bad_string)                                   # Output: I said "Wow!"



