"""Write a Python script to:

Get the user's name, age and DOB.
Print the user's name, age and DOB to the screen
If time, see if you can:

prompt the user and get the input on the same line
see if you can print "Hi " on the one line
"""

name = input("Enter your name: ")                   # Get the users name, age and DOB.
age = input("Enter your age: ")
dob = input("Enter your date of birth (DD/MM/YYYY): ")

print(f"Name: {name}")                              # Print the users name, age, and DOB to the screen.
print(f"Age: {age}")
print(f"Date of Birth: {dob}")

# Prompt the user and get the input on the same line.
name, age, dob = input("Enter your name, age, and date of birth (DD/MM/YYYY) separated by commas: ").split(',')

# Print "Hi" on a different line: \n
print(f"Hi {name},\nyou are {age} years old and your date of birth is {dob}.")


"""
Mixing the data about a user into a list:
- Use your code from the "Task: Get name, age and DOB details from a user". 
- Mix the name, age and DOB into one list user_details_list 
- Print the user's name, age and DOB from the list 
- Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list. 
- Ask the user for their height in cm and save it to the variable height 
- Save height as a float in the list, and print the height from the list. 
"""

user_details_list = [name, age, dob]                         # Putting the user data into the same list.

print(f"Name: {user_details_list[0]}")                       # [0] = name, [1] = age, [2] = dob.
print(f"Age: {user_details_list[1]}")
print(f"Date of Birth: {user_details_list[2]}")              # Printed the user's name, age, and dob from the list.

if type(user_details_list[1]) is not int:                    # Using type() to check if [1] is saved as an integer.
    user_details_list[1] = int(user_details_list[1])         # Converting the integer and updating the list.
    print(type(user_details_list[1]))                        # Outcome: <class 'int'>

# Ask the user for their height in cm and save it to the variable height
height = float(input("Enter your height in cm: "))

user_details_list.append(height)                             # We have added 'height' onto the list.
print(user_details_list)                                     # The height is saved as a float in the list (see code above).
                                                             # Output: [name, age, dob, height].

print(f"Height: {user_details_list[3]}cm.")                  # This prints out the users height.


# There is a simpler way to do this (Angy's example)
# imputs x 4
# user_details_list = [put them here)
# print
