"""Objective

Practice creating sets, adding and removing elements, and understanding the properties of sets.

The task

Explain 2 main ways that sets are different to lists and tuples
- Create a set named 'fruits' containing "apple", "banana", and "cherry".
- Print the set 'fruits'
- Add "orange" to the fruits set using one of the set's methods.
- Print the set 'fruits' - check it's added
- Remove "banana" from the fruits set using one of the set's methods.
- Print the set 'fruits' - check it's removed
- Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
- Print the final fruits set.
- Print the 2nd item in the set. If there is any problem doing this, explain.
"""

"""What are sets?"""
# Sets {} are used to store multiple items in a single variable: they are unordered.
# They are not indexed (not ordered), so you can't find anything as simply as in dictionaries.

"""Explain 2 main ways that sets are different to lists and tuples."""
# 1. Unordered: you can't be sure of the orders the items will appear. | | lists & tuples have a defined order.
# 2. Mutable: you can remove and add items, like lists. | | tuples are immutable.
# 3. Unique: sets can't have two items with the same value | | lists & tuples can contain duplicates.


fruits = {"apple", "banana", "cherry"}                  # created set
print(fruits)                                           # Output: {'apple', 'banana', 'cherry'}

fruits.add("orange")                                    # add "orange" to the set.
print(fruits)                                           # Output: {'cherry', 'apple', 'orange', 'banana'}

fruits.remove("banana")                                 # remove "banana" from the set (you can also use 'discard')
print(fruits)                                           # Output: {'apple', 'orange', 'cherry'}

fruits.add("apple")                                     # attempt to add another "apple"
print(fruits)                                           # Output is the same as above.

# What do you observe? Why does this happen?
# Because a set doesn't let you add in duplicates.

"""Print the 2nd item in the set. If there is any problem doing this, explain."""
# Sets are unordered, so you cannot access items by index. This will result in an error.

try:
    print(fruits[1])                                    # This is where we've tried to access the second item.
except TypeError as e:                                  # 'except' catches the error and prints a message dependent on the result. 
    print("Error:", e)                                  # Because sets don't have an order, we use "TypeError"
    print("Sets do not support indexing. They are unordered collections.")



