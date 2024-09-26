"""# Rationale: To practice lists
Script should act like a waiter at a restaurant taking orders

level 1
- Greet the user
- Print a list of starters
- Take an input for the user for their starter
- Print a list of mains
- Take an input for the user for their main course
- Print a list of desserts
- Take an input for the user for their dessert
- Print all of the user's choices

level 2
- Use at least one f-string
- Add each item ordered to a list called 'customer_order_list'

level 3 (may need research if we have not covered dictionaries yet)
- Use dictionaries and assign prices to the items. Create a bill at the end of the program.

level 4
- Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
"""

print("Hello, and welcome to Georgia's Restaurant!")                # greet the user.

starters = ["Soup", "Mozzerella Dippers", "Garlic Bread"]           # print a list of starters
print("Starters:", starters)                                        # Output: Starters: ['Soup', 'Mozzerella Dippers', 'Garlic Bread']

starter_choice = input("What starter would you like? ")              # Take an input for the user for their starter.

mains = ["Sirloin Steak", "Chicken & Bacon Carbonara", "Vegetarian Wellington"]     # print a list of mains.
print("Main Courses:", mains)

main_choice = input("Please choose a main course: ")                # input for user.

desserts = ["Ice Cream", "Chocolate Fudge Cake", "Fruit Salad"]     # print a list of desserts.
print("Desserts:", desserts)

dessert_choice = input("Please choose a dessert: ")                 # input for user.

# print all of the user's choices.
print(f"Brilliant! So we have: {starter_choice} for the starter, {main_choice} for the main, and {dessert_choice} for desert.")



"""Level 2: Using f-strings and Adding to a List"""

customer_order_list = [starter_choice, main_choice, dessert_choice]                     # Add each item ordered to a list called 'customer_order_list'

print(f"Brilliant! So we have: {starter_choice} for the starter, {main_choice} for the main, and {dessert_choice} for desert.")
print(f"Your complete order list: {customer_order_list}")                               # Output: Your complete order list: ['soup', 'sirloin steak', 'fruit salad']



"""Level 3: Using Dictionaries and Creating a Bill"""

print("Welcome to Georgia's restaurant!")                                           # Greet the user.

menu = {                                                                            # Define the menu with prices.
    "starters": {"Soup": 5, "Mozzerella Dippers": 4, "Garlic Bread": 6},
    "mains": {"Sirloin Steak": 20, "Chicken & Bacon Carbonara": 15, "Vegetarian Wellington": 18},
    "desserts": {"Ice Cream": 4, "Chocolate Fudge Cake": 5, "Fruit Salad": 3}
}

# TO MAKE IT SIMPLER: could you have two separate dictionaries? item & cost. As long as it's in the right order.

print("Starters:", list(menu["starters"].keys()))                                   # Print a list of starters.

starter_choice = input("What starter would you like? ")                             # User input for starters.

print("Main Courses:", list(menu["mains"].keys()))                                  # Print a list of mains.

main_choice = input("Any mains catch your eye? ")                                   # User input for mains.

print("Desserts:", list(menu["desserts"].keys()))                                   # Print a list of desserts.

dessert_choice = input("And for dessert? ")                                          # User input for dessert.

customer_order_list = [starter_choice, main_choice, dessert_choice]                 # Added items into list called 'customer_order_list'.

total_bill = menu["starters"][starter_choice] + menu["mains"][main_choice] + menu["desserts"][dessert_choice]          # Calculate the bill.


# Print user's choices and the total bill:
print(f"Brilliant! So we have: {starter_choice} for the starter, {main_choice} for the main, and {dessert_choice} for desert.")
print(f"Your complete order list: {customer_order_list}")
print(f"Your total bill is: £{total_bill}")


"""level 4
- Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc."""



