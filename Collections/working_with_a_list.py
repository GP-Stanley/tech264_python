"""You are now moving onto ‘collections’. Suggestion: Make a new folder inside the root project folder
(or python learning folder) called ‘collections’ to store your work.

Write a Python script to:

Create a list called 'shopping_list' with the following items:
        - eggs
        - bread
        - bananas
        - biscuits
        - milk
- Print the list to the screen
- Print the data type of 'shopping_list'
- Print the first item in the list
- Print the last item in the list
- Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item
    to the screen to prove it's been changed/
- Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='),
    then check the length of the list (which should now have 6 rather than 5)
- Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list.
    Use one of the list's methods to add the two items in one go.
- Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.
- Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.
- Remove the last item ('coffee') from 'shopping_list' using the pop method.
    Check it worked by printing 'shopping_list'
"""

"""Create a list"""

shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_list)

# Print the data type of 'shopping_list'
print(type(shopping_list))                          # Outcome: <class 'list'>

# Print the first item in the list
print(shopping_list[0])                             # eggs

# Print the last item in the list
print(shopping_list[-1])                            # milk

# Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item
#     to the screen to prove it's been changed/

shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

# replace all occurrences of 'bread' with 'rice'
for i in range(len(shopping_list)):                     # using a loop to go through the list: range(len(fruits)) creates a sequence of numbers from 0 to the length of the list minus one.
    if shopping_list[i] == "bread":                     # this checks if "bread" is in the list ???
        shopping_list[i] = "rice"                       # if the item is a match, it changes it to the desired item.
print(shopping_list)                                    # shows the updated list where "bread" is now "rice".

print(shopping_list[1])                                 # Output: 'rice'.


# Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='),
#     then check the length of the list (which should now have 6 rather than 5)

# .append = add/edit

shopping_list.append("carrots")                         # The 'carrot' has been added.
print(len(shopping_list))                               # Output: 6

# Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list.
#     Use one of the list's methods to add the two items in one go.

# extend() = allows you to add multiple items to a list.

shopping_list.extend(["toffee","coffee"])               # 'toffee' and 'coffee' are added.
print(len(shopping_list))                               # Output: 8

# Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.

# .remove() = can remove items from a list.

shopping_list.remove("bananas")                         # .remove() had removed bananas.
print(shopping_list)                                    # Outcome: ['eggs', 'rice', 'biscuits', 'milk', 'carrots', 'toffee', 'coffee']


#  Remove the last item ('coffee') from 'shopping_list' using the pop method.
#     Check it worked by printing 'shopping_list'

# pop method: used to remove the last item from a list at a specified position and return that item.
# If no position is specified, it removes and returns the last item in the list.

last_item = shopping_list.pop()
print(last_item)                                        # this displays the last item (coffee).
print(shopping_list)                                    # Outcome: ['eggs', 'rice', 'biscuits', 'milk', 'carrots', 'toffee']

# ^^ this pop method can be used for second_item, third_item, fourth_item and so on...