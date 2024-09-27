# Mini-calculator

def add(x, y):
    return x + y


first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = add(first_num, second_num)print(f"{first_num} + {second_num} = {result}")

-------------------------------------------------------------------------------------------

import this
# Python enhancement proposal
# PEP 20
# These principles can make you better at code.

import random

print(random.randrange()) # get a numbe rbetween 0 & 1

-----------------------------------------------------------------

import random

print(random.randrange(1, 10)) # get a numbe rbetween 1 & 10

----------------------------------------------------------------

from random import random

print(random())

----------------------------------------------------------------

import math

num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)

# gives us remainder of the 2 values
# 5 can't go into 1, so the remainder is 1

print(f"Remainder from 1/5: {math.remainder(1, 5)}")

-----------------------------------------------------------

import os
# returns our current working directory
working_directory = os.getcwd()
print(f"Current working directory: {working_directory}")

username = os.environ.get('USERNAME') or os.environ.get('USER')         # covers windows (USERNAME) or linux (USER)
print(f"The current user is: {username}")

cpu_cores = os.cpu_count()
print(f'Total CPU cores: {cpu_cores}')

# Output:
# Current working directory: C:\Users\georg\OneDrive - Sparta Global\Documents\GitHub Repos\tech264_python\learning_python\modules_libraries_packages.m
# The current user is: georg
# Total CPU cores: 12

# change directory - must exist
os.chdir("<folder_name>")

# make a new directory
os.mkdir("<folder_name>")

----------------------------------------------------------------------------------------------

import datetime
# gives us today's date

print(f"Today's date: {datetime.date.today()}")

# Output: Today's date: 2024-09-27
----------------------------------------------------------------------------------------------

import datetime
# gives us today's date

print(f"Today's date: {datetime.datetime.now()}")

# Output: Today's date: 2024-09-27 14:55:09.296038
----------------------------------------------------------------------------------------------

import builtins                                         # lists all the functions
for name in dir(builtins):
    if name[0].islower():
        print(name)

----------------------------------------------------------------------------------------------



