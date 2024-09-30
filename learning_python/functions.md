# Creating a Function
* In Python a function is defined using the `def` keyword.

```python
def my_function():
  print("Hello from a function")
```

## Calling a Function
* To `call a function`, use the `function name` `followed by parenthesis`.
```python
def my_function():
  print("Hello from a function")

my_function()           # Output: Hello from a function.
```

## Arguments
* `Information` can be `passed into functions as arguments`. 
* Arguments are specified `after the function name`, `inside the parentheses`. You can `add as many arguments` as you want, just `separate them with a comma`.
* `Arguments` are often shortened to `args` in Python documentations.
* The terms `parameter` and `argument` can be used for the `same thing`: information that are passed into a function.

The following example has a function with one argument (fname). 
When the function is called, we pass along a first name, which is used inside the function to print the full name:
```python
def my_function(fname):         # Output: a function with one argument (fname). 
  print(fname + " Refsnes")     # When you call this function with different names, it prints each name followed by " Refsnes".

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Output:
# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes
```

## Number of Arguments
* By default, a `function` must be `called with the correct number of arguments`. 
* Meaning that if your `function expects 2 arguments`, you have to `call the function with 2 arguments`, not more, and not less.
```python
# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")          # Output: Emil Refsnes
```

## Arbitrary Arguments, `*args`
* If you `do not know how many arguments` that will be passed into your function,` add a * before the parameter` name in the function definition. 
* This way the `function will receive a tuple of arguments`, and can `access the items accordingly`. 
* If you do not know how many keyword arguments that will be passed into your function, add two asterisk: `**` before the parameter name in the function definition.
```python
# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):     #  defines a function named my_function that can take any number of arguments. Inside the function, kids is treated as a tuple containing all the arguments passed to the function.
  print("The youngest child is " + kids[2])     # prints out the third argument in the kids tuple. 

my_function("Emil", "Tobias", "Linus")          # Output: The youngest child is Linus.

"""
Explanation:
The arguments "Emil", "Tobias", and "Linus" are passed to the function. 
Inside the function, kids becomes ("Emil", "Tobias", "Linus").

kids[0] is "Emil"
kids[1] is "Tobias"
kids[2] is "Linus"
"""
```

## Keyword Arguments
* You can also send arguments with the key = value syntax. 
* This way the order of the arguments does not matter.
```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")       # Output: The youngest child is Linus.
```

## Passing a List as an Argument
* You can send any `data types` of argument to a function (string, number, list, dictionary etc.), and it will be `treated as the same data type inside the function`. 
* E.g. if you send a List as an argument, it will still be a List when it reaches the function.
```python
def my_function(food):      #  defines a function named my_function that takes one parameter called food.
  for x in food:            # for loop that goes through each item in the food list.
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)     # calls the my_function and passes the fruits list to it.
                        # The function will then execute the for loop, printing each fruit in the list.
# Output:
# apple
# banana
# cherry
```

## Return Values
* To let a function return a value, use the return statement.
```python
def my_function(x):
  return 5 * x

print(my_function(3))           # Output: 15
print(my_function(5))           # Output: 25
print(my_function(9))           # Output: 45
```













