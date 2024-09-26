## Understanding Operators and Operand

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



### Operators
Operators are symbols that tell the computer to perform specific tasks, like addition or comparison.
```python
a = 5
b = 1

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

### Operands
Operands are the values or data that operators act on (for example) a, b.


## Comparison Operators

| Operator | Meaning                |
|----------|------------------------|
| ==       | Equal to               |
| !=       | Not equal to           |
| <        | Less than              |
| >        | Greater than           |
| <=       | Less than or Equal to  |
| >=       | Greater than or Equal to |

```python
a = 5
b = 1

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b) 
print(a <= b)
```

### Logical operators = used on conditional statements

> and = checks two or more conditions if True 
> 
> or = checks if at least one condition is True 
> 
> not = True if condition is False, and vice versa


#### AND EXAMPLE
> checking if multiple conditions are True.
```python
temp = -25

if temp > 0 and temp < 30: 
    print("The temperature is good.")
else:
    print("The temperature is bad.")
```

#### OR EXAMPLE
> checking if at least one condition is True.
```python
temp = 40

if temp <= 0 or temp >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")
```

#### NOT EXAMPLE
> 'not' will change something from False to True and vice versa.
> 
> checking if at least one condition is True.
> 
> 'not' will change something from False to True and vice versa.

```python
temp = 20
sunny = True                                

if temp <= 0 or temp >= 30:    
    print("The temperature is bad.")
else:
    print("The temperature is good.")

if not sunny:                   
    print("It is cloudy outside.")
else:
    print("It is sunny outside.")
```