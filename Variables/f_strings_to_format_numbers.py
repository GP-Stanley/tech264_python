"""Code to get you started:

pi = 3.14159265359

- Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
- Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'


score = 16
max_score = 26
score_as_decimal = score/max_score


- Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
- Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
- Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
- Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'"""

# f-string: allows you to put variables inside the string.


# Formatting Specifier :.3f:
# Inside the curly braces {}, the expression pi:.3f is used to format the value of pi.
# : indicates that a format specification follows.
# .3f is the format specification:
# .3 specifies the precision, meaning three digits after the decimal point.
# f stands for fixed-point notation, which means the number will be formatted as a decimal number.

"""Task 1"""
pi = 3.14159265359

# print pi to 3 decimal places

print(f"Pi to 3 decimal places is: {pi:.3f}")               # Outcome: Pi to 3 decimal places is: 3.142

# Explanation: {pi:.3f} : tells Python to take the value of 'pi' and show it with 3 numbers after the decimal point.
# using f-strings and the .3f or .5f format, you can control how many decimal places you want to show for the number pi.


# print pi to 5 decimal places
print(f"Pi to 5 decimal places is: {pi:.5f}")               # Outcome: Pi to 3 decimal places is: 3.14159



"""Task 2"""
# DON'T FORGET: To convert a decimal to a percentage, you multiply by 100.
score = 16
max_score = 26
score_as_decimal = score/max_score

# Use an f-string to print 'score_as_decimal'
print(f"You scorced {score_as_decimal}!")

# Use an f-string to print 'score_as_decimal' formatted as a percentage
print(f"You scorced {score_as_decimal * 100}%")

# percentage rounded to 2 decimal places
print(f"You scorced {score_as_decimal:.2%}")

# 'f' is replaced by the %, they do not work together.

# percentage to rounded to a whole number
print(f"You scorced {score_as_decimal:.0%}")

print(f'You scored {score_as_decimal:.2%}')