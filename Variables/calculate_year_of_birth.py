from datetime import datetime
"""First part
- Define the variables age_int and name_str (set dummy/default/initial values)
- Make a calculation for the year in which the person was born
- Print out "OMG , you are years old so you were born in " with the correct values

Second Part
- Prompt the user for inputs and assign the variable age_int and name_str
- Remove the initial values set

Third Part
- calculate and print out the total number of hours this person has lived

If time
- Figure out a way to account for if the persons birthday has already happened this year or not
- Go look into the library 'time' to be more accurate with the hours lived
- Show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate

Acceptance Criteria
- Program defines the variable age_int and name_str
- Program prints the string "OMG <person>, you are <age> years old so you were born in <year>"
 """

"""First Part"""

age_int = 38
name_str = "John Doe"

current_year = 2024
year_of_birth = current_year - age_int

# print(f"OMG {name_str}, you are {age_int} years old so you were born in {year_of_birth}.")


"""Second Part"""
name_str = input("Enter your name: ")
age_int = int(input("Enter your age: "))

year_of_birth = current_year - age_int

print(f"OMG {name_str}, you are {age_int} years old so you were born in {year_of_birth}.")


"""Third Part"""

# Prompt the user for their date of birth
dob_str = input("Enter your date of birth (DD/MM/YYYY): ")
dob = datetime.strptime(dob_str, "%d/%m/%Y")

# Get the current date and time
now = datetime.now()
current_year = now.year

# Calculate the total number of hours lived
age_in_days = (now - dob).days
hours_lived = age_in_days * 24

# Print the total number of hours lived
print(f"OMG {name_str}, you have lived for approximately {hours_lived} hours.")


"""If Time"""

# Check if the birthday has already happened this year
birthday_this_year = dob.replace(year=current_year)
if now < birthday_this_year:
#    age_int -= 1
    print("Your birthday hasn't happened yet!")
else:
    print("I hope you enjoyed your birthday!")
# Update year_of_birth after adjusting age_int
year_of_birth = current_year - age_int

