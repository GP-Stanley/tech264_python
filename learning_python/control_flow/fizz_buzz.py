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