## Use `while loop` to verify user input of age
1. Loop until age is all digits 

Look at this code:
``` python
# Ask user for their age 
age = input("What is your age? ") 
print(f" Your age is {age}") 
``` 

The problem with this code is that even if the user is 20, they could enter "20" or "twenty". 
Let's standardise the input to get the age as digits... 

**Hints**: To check is 'age' is all digits, use the 'age' string's method `.isdigit() `

Starting code - replace comments in CAPITALS with your code: 

``` python
user_prompt = True                                  # remember it's a capital 'T'
while user_prompt:
    age = input("What is your age? ") 
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age as a number.")
 
print(f"Your age is {age}") 
``` 
2. Also check age is in the correct range 

Our code now works to stop our user from inputting `strings`, `floats`, and `negative numbers`, but at the moment the user could say they are 356000 years old if they want.
Assuming the oldest person alive today is 117, modify your code to only allow a maximum of 117 as the age. 

Hint: You already have an 'if statement' to check 'age' is all digits. Use the 'and' keyword to ALSO check 'age' is not too high.

```python
user_prompt = True                              # remember it's a capital 'T'
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) <= 117:       # making sure the 'age' is a number and less than equal to (<=) 117.
        user_prompt = False
    else:
        print("Please enter a valid age.")

print(f"Your age is {age}")
```
### Explanation:
* `user_prompt = True` starts the process by setting a flag to keep asking for input.
* `while user_prompt:` keeps looping as long as `user_prompt is True`.
* `age = input("What is your age? ")` asks the user to enter their age.
* `if age.isdigit() and int(age) <= 117:` checks if the entered age is made up of digits only and is not greater than 117.
* `user_prompt = False` stops the loop.
* If the input is not a number or is greater than 117, `print("Please enter a valid age as a number (0-117).")` tells the user to enter a valid number within the specified range.

This way, the user is prompted until they provide their age in digits and within the valid range, ensuring the input is correct.
