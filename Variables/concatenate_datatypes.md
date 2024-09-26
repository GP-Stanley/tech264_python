# Concatenate Datatypes

Explain: What is concatenation? Give a simple example with your code.
Your starting code:
```python
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print(x + y + z)
```

* This should not work. Make it work:
* Make the print statement work using concatenation (+) to join x, y and z so that it prints this to the screen: `25.4 there's now a number 25.4 unless we put a space in!"
* Explain: The problem and the solution"""

> Concatenate: to join things together.

We need to convert x and y strings and then concatenate.
```python
x = 2                           
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

result = str(x) + str(y) + z
print(result)
```

### Why are they converted separately?
Converting x and y separately ensures that each number is treated as a string before being joined.

If you don’t convert them separately, the addition operation will be performed first,
and then the result will be converted to a string.