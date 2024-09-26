"""Before finishing the game below, answer these questions:

- How are tuples similar to lists?
- Are tuples immutable and what does this mean?
- What other data types are immutable?
- What is a good use case for tuples?
- What does the following piece of code do?
```

essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))

```

Objective
- Practice using tuples.

The task
- Add your code where it says 'YOUR CODE GOES HERE'

Starting code:

```

"Stranded on a Desert Island" game
Rationale: Practice tuples
Type of exercise: Finish the code

- print("You are stranded on a desert island. You can take only THREE items.")
- essential_item1 = input("What is an essential item you would take? ")
- essential_item2 = input("What is an essential item you would take? ")
- essential_item3 = input("What is an essential item you would take? ")

save the items as a tuple

- essentials_tuple = None  # YOUR CODE GOES HERE INSTEAD OF 'None'

print the tuple

print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")

- try to add the 4th item to the tuple
- if you can't add the 4th item, work out how to save the 4th item to the tuple

# YOUR CODE GOES HERE

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)

"""

"""How are tuples similar to lists?"""
# Both store multiple items.
# They can contain items of different data types.
# Both have a defined order and can be accessed via their index.

"""Are tuples immutable and what does this mean?"""
# Yes.
# They cannot be changed, added, or removed.

"""What other data types are immutable"""
# Strings (sequence of characters)
# Integer (whole numbers)
# Floats (decimal numbers)
# Frozensets() -  a set of items that you can’t change once you’ve created it. e.g., vowels.

"""What's a good use for tuples?"""
# When you want to store items that will NOT change throughout the program.
# e.g., vowels, database records, co-ordinates (location: lat, lng).

"""What does the following piece of code do?"""

essentials = ("bread", "eggs", "milk")              # created a tuple: list of items.
print(essentials)                                   # prints the items in the list.
print(essentials.count("bread"))                    # prints how many times " " appears in the list. i.e., bread = 1.


"""Desert Island Game"""
# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code


print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")

essentials_tuple = (essential_item1, essential_item2, essential_item3)              # Save the items as a tuple.
print("Here are your items: ", essentials_tuple)                                    # Show tuple list to user.

print("")
print("I lied. You can take one more item.")

essential_item4 = input("What is one more essential item you would take? ")

# essentials_tuple = essentials_tuple + (essential_item4,)                          # How to add to the already saved tuple.
                                                                                    # Why the comma? tells Python that this is a tuple containing one element, essential_item4.

new_tuple = (essential_item1, essential_item2, essential_item3, essential_item4)    # Simpler way to do this ^^


print("Here are your items with the additional item:", new_tuple)

