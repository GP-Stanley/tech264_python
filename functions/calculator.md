## Importing example: calculator

```python
from math_operations import *
# ^^ from <module> (a single file), import the functions.
# a library is a set of modules (files).
# a module is a single file imported.
# a package is installable. A module or a library can become a package if its installable.

# Mini-calculator

# first_num = int(input("Enter the first number: "))
# second_num = int(input("Enter the first number: "))
# result = add(first_num, second_num)

# print(f"{first_num} + {second_num} = {result}")

import math_operations as mo            # 'mo' mean module.
                                        # This part assigns the alias mo to the math_operations module.
                                        # With this name, you can call functions using the shorter name, like mo.add(5, 3).

# Testing the functions from math_operations module
print("Addition of 5 and 3:", mo.add(5, 3))         # Output: 8
print("Subtraction of 5 and 3:", mo.subtract(5, 3)) # Output: 2
print("Multiplication of 5 and 3:", mo.multiply(5, 3)) # Output: 15
print("Division of 5 by 3:", mo.divide(5, 3))       # Output: 1.6666666666666667
print("Exponentiation of 2 to the power of 3:", mo.exponentiate(2, 3))  # Output: 8
print("Evaluation of expression '2 + (3 - 1) * 5':", mo.evaluate_expression("2+(3-1)*5"))  # Output: 12
```



## Complete a viable basic calculator using functions.

### Math Operators

| Operators | Operation           | Example     |
|-----------|---------------------|-------------|
| **        | Exponent            | 2 ** 3 = 8  |
| %         | Modulus/Remainder   | 22 % 8 = 6  |
| //        | Integer division    | 22 // 8 = 2 |
| /         | Division            | 22 / 8 = 2.75 |
| *         | Multiplication      | 3 * 3 = 9   |
| -         | Subtraction         | 5 - 2 = 3   |
| +         | Addition            | 2 + 2 = 4   |


MVP (each of these should be in a separate function):
* Can add 2 numbers
* Can subtract 2 numbers
* Can multiply 2 numbers
* Can divide 2 numbers
 """
```python
# Function to add two numbers.
def add(a, b):
    return a + b

# Function to subtract two numbers.
def subtract(a, b):
    return a - b

# Function to multiply two numbers.
def multiply(a, b):
    return a * b

# Function to divide two numbers.
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."


print("Addition of 8 and 4:", add(8, 4))
print("Subtraction of 8 and 4:", subtract(8, 4))
print("Multiplication of 8 and 4:", multiply(8, 4))
print("Division of 8 by 4:", divide(8, 4))
print("Division of 8 by 0:", divide(8, 4))
```

### Taking it to the next level: 
* Implement more complex operations, such as handling parentheses, exponentiation 
* More advanced operations should continue to be broken into separate functions 

## Exponentiation
* `exponentiate`
* `**`
* Takes two arguments `base` and `exponent`.
* Returns the result of raising base `to the power` of exponent.

```python
def exponentiate(base, exponent):
    return base ** exponent

# Testing the exponentiation function (2^3 = 8)
print("Exponentiation of 2 to the power of 3:", exponentiate(2, 3))  # Output: 8
```

## Handling Parentheses
* `evaluate_expression`
* Uses a recursive approach to `evaluate expressions within parentheses`. 
* Parses the `expression` and evaluates it step by step, handling nested parentheses.
* An `expression` in Python is a combination of operators and operands. An example of expression can be : `x = x + 1 0 x = x + 10 x=x+10`. 

## Parsing logic
* Digit Handling: 
  * If the current character is a digit, it updates `num` by multiplying the current `num` by 10 and adding the integer value of the character. This handles multi-digit numbers. 
* Plus and Minus Handling: 
  * If the current character is `+,` it adds the current `num` (considering the `sign`) to `result`, resets `num` to 0, and sets `sign` to 1. 
  * If the current character is `-`, it does the same but sets sign to `-1`.
* Parentheses Handling:
  * If the current character is `(`, it finds the corresponding `)` by tracking the balance of parentheses.
  * It then recursively calls `parse_expression` on the substring within the parentheses and assigns the result to `num`.
* Closing Parenthesis Handling:
  * If the current character is `)`, it adds the current `num` (considering the `sign`) to `result` and returns `result`.
* End of Expression:
  * After the loop, it adds any remaining `num` (considering the `sign`) to `result`.
* Final Return:
  * The outer function `evaluate_expression` calls `parse_expression` with the input expression and returns the result.

## Example
For the expression `1 + (2 - 3)`, the function would:
* Parse `1`, add it to `result`.
* Encounter `+`, set `sign` to 1.
* Encounter `(`, recursively parse `2 - 3`, which results in `-1`.
* Add `-1` to `result`, resulting in `0`.

### End result: calculator
```python
# mini calculator.
def add(x, y):
    return x + y

# Function to subtract two numbers.
def subtract(a, b):
    return a - b

# Function to multiply two numbers.
def multiply(a, b):
    return a * b

# Function to divide two numbers.
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# to the power of
def exponentiate(base, exponent):
    return base ** exponent


def evaluate_expression(expression):                # takes a mathematical expression as a string and evaluates it.
    def parse_expression(expr):                     # does the parsing and evaluation of the expression.
        stack = []                                  # stack: used for handling nested expressions.
        num = 0                                     # stores the current number being processed.
        sign = 1                                    # stores the current sign (1 = pos, -1 = neg).
        result = 0                                  # accumulates the result of the expression.
        i = 0                                       # index: to traverse the expression string.

        while i < len(expr):                        # this loop iterates through each character in the expression (expr).
            char = expr[i]

            if char.isdigit():                      # digit handling: If the character is a digit, it updates num by shifting the current num left by one decimal place (multiplying by 10) and adding the new digit.
                num = num * 10 + int(char)
            elif char == '+':                       # addition handling: If the character is a ‘+’, it adds the current num to result (considering the current sign), resets num to 0, and sets sign to 1 (positive).
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':                       # subtraction handling: If the character is a ‘-’, it adds the current num to result (considering the current sign), resets num to 0, and sets sign to -1 (negative).
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':                       # paranthesis handling: If the character is ‘(’, it finds the corresponding closing ‘)’ by maintaining a balance counter. It then recursively evaluates the expression inside the parentheses using parse_expression.
                j = i
                balance = 0
                while i < len(expr):
                    if expr[i] == '(':
                        balance += 1
                    if expr[i] == ')':
                        balance -= 1
                    if balance == 0:
                        break
                    i += 1
                num = parse_expression(expr[j + 1:i])
            elif char == ')':                           # closing paranthesis handling: If the character is ‘)’, it adds the current num to result and returns result.
                result += sign * num
                return result
            i += 1                                      # increment index: Moves to the next character in the expression.

        result += sign * num                            # final addition: After the loop, it adds the last num to result and returns result.
        return result

    return parse_expression(expression)                 # entry point: This is the entry point of the function, which starts the parsing process.
```



### Constant Expressions
* Expressions that have constant values only.
```python
# Constant Expressions 
x = 15 + 1.3
  
print(x)                # Output: 16.3
```
### Arithmetic Expressions
* Combination of numeric values, operators, and sometimes parenthesis.
* The result is also a numeric value.
* The operators used in these expressions are arithmetic operators like addition, subtraction, etc.

| Operators | Syntax  | Functioning      |
|-----------|---------|------------------|
| +         | x + y   | Addition         |
| –         | x – y   | Subtraction      |
| *         | x * y   | Multiplication   |
| /         | x / y   | Division         |
| //        | x // y  | Quotient         |
| %         | x % y   | Remainder        |
| **        | x ** y  | Exponentiation   |

### Relational (Boolean) Expressions
* Arithmetic expressions are written on both sides of `relational operator` (`>` , `<` , `>=` , `<=`). 
* Arithmetic expressions are evaluated first, and then compared as per `relational operator` and produce a `boolean` output in the end.

```python
# Relational Expressions 
a = 21
b = 13
c = 40
d = 37
  
p = (a + b) >= (c - d) 
print(p)
```

### Logical Expressions
* Result in either `True` or `False`.
* It  specifies one or more conditions. 
  * For example, (10 == 9) is a condition if 10 is equal to 9. 
  *  It is not correct, so it will return False.

| Operator | Syntax  | Functioning                                                      |
|----------|---------|------------------------------------------------------------------|
| and      | P and Q | It returns true if both P and Q are true; otherwise returns false|
| or       | P or Q  | It returns true if at least one of P and Q is true               |
| not      | not P   | It returns true if condition P is false                          |

```python
P = (10 == 9) 
Q = (7 > 5) 
  
# Logical Expressions 
R = P and Q 
S = P or Q 
T = not P 
  
print(R) 
print(S) 
print(T)

# Output: 
# False
# True
# True
```

### Bitwise Expressions
* computations are performed at bit level.

```python
# Bitwise Expressions 
a = 12
  
x = a >> 2
y = a << 1
  
print(x, y)                 # Output: 3 24
```
### Combinational Expressions
* Different types of expressions in a single expression.

```python
# Combinational Expressions 
a = 16
b = 12
  
c = a + (b >> 1) 
print(c)                    # Output: 22
```




