Write a Python script to:

* Get the user's name, age and DOB.
* Print the user's name, age and DOB to the screen. 

If time, see if you can:
* prompt the user and get the input on the same line.
* see if you can print "Hi " on the one line.
```python
name = input("Enter your name: ")                   
age = input("Enter your age: ")
dob = input("Enter your date of birth (DD/MM/YYYY): ")
```
#### Get the users name, age and DOB.
> Print the users name, age, and DOB to the screen.
```python
print(f"Name: {name}")                              
print(f"Age: {age}")
print(f"Date of Birth: {dob}")
```

#### Prompt the user and get the input on the same line.

> name, age, dob = input("Enter your name, age, and date of birth (DD/MM/YYYY) seperated by commas: ").split(',')

#### Print "Hi" on a different line: \n
```python
print(f"Hi {name},\nyou are {age} years old and your date of birth is {dob}.")
```