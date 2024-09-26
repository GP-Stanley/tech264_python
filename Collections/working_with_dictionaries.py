"""Make a dictionary called "student_1" containing the following information:
    name: susan
    stream: tech
    completed_lessons: 4 (should be saved as an integer not a string)
    completed_lesson_names: value should be list of these 3 items: "variables", "data_types", "set up"

Explain how a dictionary saves/structures data? Example, what does each value need to be accompanied/associated with?
- Print the dictionary to the screen
- Print it's data type to the screen to check it's a dictionary
- Print the value for the key-value pair having the key "stream"
- Print the value for 'completed_lesson_names' - check you can see the list of 3 items
- Print the data type for the value for 'completed_lesson_names' - check it is a list
- Print the first element/item in the list of 'completed_lesson_names' (should output "variables")
- Change the value of "completed_lessons" to 3 (an integer not string). Make sure you change was successful by printing
    your dictionary to the screen again.
- Delete "data_types" from the list under the key 'completed_lesson_names'
- Use the keys() method on your dictionary to list all the keys
"""

"""Key Definitions"""
# Dictionary - dict() - an unordered data collection in a key: you can store key-value pairs.

# Key-value pairs - Each item in a dictionary has a key and a value. The key is used to access the corresponding value.

# Mutable - you an change, add, or remove items after the dictionary is created.

# Ordered - dictionaries are ordered in the same way they were added.

# No duplicate keys - each key MUST be unique.
#   If you try to add an item with a key that already exists, the old value will be replaced with the new one.

"""Explain how a dictionary saves/structures data?"""
# It stores information in pairs: info (value) and a unique name (key)
# e.g., phone contact needs a name (key) and a number (value).
# Helps you find and use data based on a unique key, quickly.

student_1 = {                                         # This is how you create a dictionary (key-value pairs).
    "name" : "Alice",
    "stream" : "Tech",
    "completed_lessons" : 4,                          # This is saved as an integer.
    "completed_lesson_names" : ["variables", "data_types", "set up"]            # This is the list of 3 items.
}

print(student_1)                                      # Printed the dictionary.
# Output: {'name': 'Alice', 'stream': 'Tech', 'completed_lessons': 4, 'completed_lesson_names': ['variables', 'data_types', 'set up']}

print(type(student_1))                                # Output: <class 'dict'>

print(student_1["stream"])                            # Output: "Tech", because you've asked it to print the value for the key "stream"

print(student_1["completed_lesson_names"])            # Output: ["variables", "data_types", "set up"], because you've asked it to print the value for 'completed_lesson_names'

print(type(student_1["completed_lesson_names"]))      # Output: <class 'list'> : you've asked it to print the data type.

print(student_1["completed_lesson_names"][0])         # Output: "variables" : you've asked it to print the first element [0]

student_1["completed_lessons"] = 3                    # Changing the value of 'completed_lessons' to 3
print(student_1)                                      # Output: {'name': 'Alice', 'stream': 'Tech', 'completed_lessons': 3, 'completed_lesson_names': ['variables', 'data_types', 'set up']}

student_1["completed_lesson_names"].remove("data_types")    # delete data_types from the list. first name the key 'completed_lesson_names'
print(student_1)                                            # Output: {'name': 'Alice', 'stream': 'Tech', 'completed_lessons': 3, 'completed_lesson_names': ['variables', 'set up']}
                                                            # 'data_types' has been removed.

print(student_1.keys())                             # the keys() list all the keys
                                                    # Output: dict_keys(['name', 'stream', 'completed_lessons', 'completed_lesson_names'])











