# fizzbuzz.py

# Loop through numbers from 1 to 100.
# for number in range(1, 101):
#
#     if number % 3 == 0 and number % 5 == 0:         # Check if the number is a multiple of both 3 and 5.
#         print("FizzBuzz")                           # The % operator gives the remainder of the division.
#                                                     # If a number is divisible by both 3 and 5, the remainder will be 0 for both.
#                                                     # If this condition is true, we print “FizzBuzz”.
#
#     elif number % 3 == 0:                           # Check if the number is a multiple of 3.
#         print("Fizz")
#
#     elif number % 5 == 0:                           # Check if the number is a multiple of 5.
#         print("Buzz")
#
#     else:
#         print(number)               # If the number is not a multiple of 3 or 5, print the number itself.


def fizzbuzz(n, fizz_num=3, buzz_num=5):            # customizable arguments.
    for i in range(1, n + 1): # starting from 1.    # n + 1: This is the ending value of the sequence. The loop will stop before it reaches this value. So, if n is 5, the loop will run with i taking values 1, 2, 3, 4, and 5.
        if i % fizz_num == 0 and i % buzz_num == 0:
            print("FizzBuzz")
        elif i % fizz_num == 0:
            print("Fizz")
        elif i % buzz_num == 0:
            print("Buzz")
        else:
            print(i)

# Example usage
fizzbuzz(100)


# i % fizz_num == 0: This checks if the current value of i is divisible by fizz_num without leaving a remainder. The % operator is the modulus operator, which returns the remainder when i is divided by fizz_num. If i % fizz_num == 0, it means i is a multiple of fizz_num.
# i % buzz_num == 0: Similarly, this checks if i is divisible by buzz_num without leaving a remainder. If this condition is True, it means i is a multiple of buzz_num.
# and: This is a logical operator that checks if both conditions are True. The code inside the if block will only run if both i % fizz_num == 0 and i % buzz_num == 0 are True.
# Overall meaning:
# This line checks if i is divisible by both fizz_num and buzz_num. If it is, the code inside the if block will execute. This is often used to detect numbers that are multiples of both fizz_num and buzz_num (for example, in the FizzBuzz game, it's used to check for numbers like 15 that are multiples of both 3 and 5).