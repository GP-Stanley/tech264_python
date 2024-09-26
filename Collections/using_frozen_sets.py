"""Objective - Understand the concept and usage of immutable sets (frozen sets).

The task
- Create a frozen set named frozen_set containing elements "hello", "world".
- Try to add "!" to frozen_set. What happens?
- Create a normal set named normal_set containing elements "let's", "learn".
- Try to add frozen_set to normal_set. Why does it work? Explain.
- Print normal_set.
- Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
What makes a frozen set different to a normal set? Explain.
"""

"""What is a frozen set?"""
# Like a regular set, but it cannot be changed after it’s created. It's “frozen” in place.

frozen_set = frozenset(["hello", "world"])                      # Creating a frozen set.


try:
    frozen_set.add("!")                                         # Try to add "!" to 'frozen_set'. What happens?
except AttributeError as e:                                     # Adding an element raises an "AttributeError" because frozensets are immutable.
    print("Error:", e)
    print("Frozen sets are immutable, so you cannot add elements to them.")


normal_set = {"let's", "learn"}                                 # Create a normal set named 'normal_set' containing elements "let's", "learn".
print("Normal set before adding frozen_set:", normal_set)       # Output: Normal set before adding frozen_set: {'learn', "let's"}


normal_set.add(frozen_set)                                      # Try to add 'frozen_set' to 'normal_set'. Why does it work? Explain.
print("Normal set after adding frozen_set:", normal_set)        # Output: Normal set after adding frozen_set: {'learn', "let's", frozenset({'hello', 'world'})}

# ^^ Why this works: frozen sets can be added to other (normal) sets.

                                                                # Print normal set.
print("Final normal set:", normal_set)                          # Output: Final normal set: {frozenset({'hello', 'world'}), 'learn', "let's"}

"""Run your script half a dozen times. 
What do you notice about where 'frozen_set' is added to 'normal_set'?
- Hint: Look at the order of the items.
(You can run this script multiple times to observe the order.)"""
# The order changes.
# sets are unordered collections (both normal and frozen)

"""What makes a frozen set different from a normal set? Explain."""
# (mutable & usage)
# Mutable - you can remove or add elements in a normal set. You can't do this with frozen sets as they're immutable.
# Usage - frozen sets can be used as keys in dictionaries (and normal sets) as they are immutable.



