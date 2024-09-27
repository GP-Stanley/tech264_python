## What is a function?
A function is a block of organised, reusable code that performs a specific task. 
* Functions help make your code more modular and easier to manage.
* You can call it or use that function whenever you need to in that code. 

## Make Functions
### 1. Make a function with no argument
* Name it 'print_something' and all it should do it print something to the screen
* Call the function to test it works

```python
def print_something():          # function is made.
    print("Hello, World!")

print_something()               # call the function.
```
### 2. Make a function with one argument
* Aim: Improve the last function by having it receive an argument to replace the 'hard coded' string
* Make a new improved function which:
  * Accepts a string variable as an argument
  * Prints the string variable received as an argument

```python
def print_something(hello):            # within the brackets is the parameters.
    print(hello)

print_something("Hello, World!")       # call the function. # these are the arguments (in brackets).
```
### 3. Make a more interesting version of a function that accepts one argument
* Here is the code to call the function:
  * greet("Susan")
* You need to write the function
* Make sure the print statement in your function uses concatenation (ie. +) rather than an f-string 
* Output should be:
  * Hello, my name is Susan.

```python
def greet(name):                            # name the argument in ().
    print("Hello, I am " + name + ".")
    
greet("Susan")                              # call the function. 
                                            # Output: Hello, I am Susan.
```
### 4. Make a function with 2 arguments that returns a value
* Troubleshoot this code so that the function returns the correct value of 4:
```python
def addition(int1, int2):
    return int1 + int2                  # add 'return' to show the result of the addition.

print(addition(2, 2))                   # given the parameters a value.      # Output: 4
```
ANOTHER WAY ??:
```python
def addition(int1, int2):
    return int1 + int2                  # add 'return' to show the result of the addition.

result = addition(2, 2)                 # these are the arguments (in brackets).
print(result)                           # Output: 4
```
* This time we do NOT want the function to do the print to the screen
* Document what you've learnt
  * The `return` statement is needed for a function to send back a result to the caller.

_________________________________________________________________________________________________________________________

### 5. Make a function with default values
1. Copy your working code from the last exercise (that adds 2 and 2 together) as starting code for this exercise
2. Replace line of code to call the function with this:
```python
def addition(int1, int2):               # within the brackets is the parameters.
    return int1 + int2                  # add 'return' to show the result of the addition.

result = addition(2, 2)                 # Output: 4

print(addition())
```
3. Run your code - you should get an error:
```python
TypeError: addition() missing 2 required positional arguments: 'int1' and 'int2'
```
4. Modify your function so that int1 and int2 both have the default value of 2
5. Run your code and make sure the result is 4
6. Now call your function with this line of code:
```python
def addition(int1=2, int2=2):           # modify function (2).
    return int1 + int2

                                        # Call the function
print(addition())                       # This should print 4
print(addition(4, 4))                   # This should print 8.      # if you write something here, it overwrites the default parameters up top. 
```
Explain why the answer is now 8:
* When no arguments are provided, the default values (2 and 2) are used, resulting in 4. 
* When arguments (4 and 4) are provided, they override the default values, resulting in 8.
* we gave the parameters fault values (int1=2).
* We override the default value. 

_______________________________________________________________________________________________________

### 6. Make a function that accepts any number of arguments
* Design a function called 'print_every_number' which accepts a tuple of numbers as an argument
* The function should do 2 things:
  * Print the type of the tuple that was passed in as an arguments
  * Loop through the tuple and print each item in the tuple on a separate line
* After calling the function, the output should be:
```python
def print_every_number(*args):      # you can pass as many numbers as you want (args), these are captured in a tuple.
    print(type(args))               # print data type.
    for num in args:                # loop through the tuple. 'n' represents each item in the tuple.
        print(num)

print_every_number(1, 2, 2, 3, 3, 4, 5, 5)


# Output: 
#<class 'tuple'>
#1
#2
#2
#3
#3
#4
#5
#5
```
Explain what character allows your function to accept multiple arguments:
* The `*` character allows the function to accept multiple arguments, which are passed as a tuple.
* `positional arguments`: the order you print the numbers matters. It will print in the same order as you asked it to.
*  `*`: will turn any number of arguments into a tuple.

_________________________________________________________________________________________________________________________________

### 7. Make a function which gives a hint about an argument's data type

Some people think stricter typing should be used with Python as best practice, let's find out why
1. See what happens if you call your earlier greet function with this line of code:
```python
greeting(24601)
```
2. To HELP us avoid this type of error, define the type of argument accepted into our function so that we are given a warning BEFORE we even run out Python script:
3. Define that data type accepted by your greet function is a string 
4. Notice that PyCharm now gives the warning Expected type 'str', got 'int' instead BEFORE you even run your code

```python
def greet(name: str):
    print("Hello, I am " + name + ".")

greet("24601")                               # this is in a string (because of the hint in the first line).  

# Output: Hello, I am 24601.
```
### 8. Make a function which gives a hint about a return value's data type

Let's make a new function to bring it all together, also to provide type hints for all arguments, function return values and variables used...

The function should be named division:
* It should divide 2 integers accepted as arguments 
* It should return the result of the division 

The arguments should:
* have their types defined 
* have the default values of 2 and 5 (therefore, by default 2 will be divided by 5 and have the result 0.4)
* NEW! Define the value returned as a float for the type hint 
* NEW! Before calling the function, define variables a and b in Python as strongly-typed integers with the values 4 and 6 

You should call the function with this line of code:
```python
print(division(a, b))
```
Also check the default values work if no values are passed into the function
```python
def divide(a : int = 2, b: int =5)-> float:           # if you call this function without a and b, the default is used. 
    return a/b

a: int = 4                                  # defined the type as an 'int'.
b: int = 6                                  # a and b both overwrite the set parameters above.

print(divide(a, b))                       # 0.6666666666666666
print(divide())                           # 0.4           # Ctrl+space: can provide you with all the options within the space in the brackets. 
```
### 9. What are some good practices when it comes to functions?
* Choose your function name wisely! Try and have it describe what it does.
* `#Comments` and `"""docstrings"""` to describe what your functions do and how they should be used.
* Keep your functions small and simple. Ideally focused on a single task.
* Try and name them using verbs - division : divide.




