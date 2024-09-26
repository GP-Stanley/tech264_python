## Working with for loops

Follow the instructions below to create various 'for loops'. 

Starting code to put at the top: 

``` python
list_data = [1, 2, 3, 4, 5] 
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}} 
``` 

1. Loop through a list 
* Under the starting code, write a _`for loop` to print the double of each number_ in the list `list_data`. 
* It should loop through the numbers in `list_data` - each item in the list should be called `num` (for number) 
* Inside the loop, it should print out the double of each number in the list. 

```python
list_data = [1, 2, 3, 4, 5] 
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}} 

for num in list_data:
    print(num * 2)

# Output: 2, 4, 6, 8, 10
``` 
### How does it know what 'num' means?
1. The `for loop` starts by taking the first element of `list_data`, which is `1`, and assigns it to the variable `num`. 
2. The loop then executes the block of code inside it, using `num` to refer to the current element. 
3. After executing the block of code, the loop moves to the next element in `list_data`, assigns it to `num`, and repeats the process. 
4. This continues until the loop has gone through all elements in `list_data`.

________________________________________________________________________________________________________________________________________________________

2. Loop through the `embedded_lists` list 
* Write another `for loop` to print the items inside of `embedded_lists`. 
* Each item in the list should be called `data` 


``` python
[1, 2, 3] 
[4, 5, 6] 

for data in embedded_lists:
    print(data)
    
# Output 
# 2
# ([1, 2, 3])
# ([4, 5, 6])
# 4
# ([1, 2, 3])
# ([4, 5, 6])
# 6
# ([1, 2, 3])
# ([4, 5, 6])
# 8
# ([1, 2, 3])
# ([4, 5, 6])
# 10
# ([1, 2, 3])
# ([4, 5, 6])
```
### How does it know what 'data' means?
1. The `for` loop iterates over each sublist in `embedded_lists`. 
2. For each sublist (`data`), it prints the sublist.

________________________________________________________________________________________________________________
3. Loop through the lists embedded inside a list
* We need to access the data within the `lists`, so now we need an `embedded loop`. 
* Create another loop inside of the `embedded_lists` for loop to list the individual items in the lists. 


``` python
list_data = [1, 2, 3, 4, 5] 
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}} 

for data in embedded_loop:
    print(data)
    for item in data:
        print(item) 

# Output:
# [1, 2, 3] 
# 1 
# 2 
# 3 
# [4, 5, 6] 
# 4 
# 5 
# 6 
```

4. Loop through a `dictionary`
* Write another `for loop` to loop through the dictionary `dict_data`.

``` python
list_data = [1, 2, 3, 4, 5] 
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}} 

for key in dict_data:
    print(key)

# Output:
# 1 
# 2 
# 3 
```
5. Loop through a dictionary and `print its values` 
* Write another for loop, to loop through the dictionary `dict_data`. 
* Use to the dictionary's `value()` method to print the value for each key in the dictionary.

``` python
list_data = [1, 2, 3, 4, 5] 
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}} 

for value in dict_data.values():
    print(value)
# Output:    
# {'name': 'Bronson', 'money': '$0.05'} 
# {'name': 'Masha', 'money': '$3.66'} 
# {'name': 'Roscoe', 'money': '$1.14'} 
``` 
6. Loop to `print the values` of the `dictionary items` `inside a dictionary` 
* Copy and paste the last for loop as a starting point for this loop. 
* Generate an `embedded for loop` (a loop within a loop) to extract and `print the values within the dictionary of each item` in the dictionary. 


``` python
list_data = [1, 2, 3, 4, 5] 
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}} 

for value in dict_data.values():
    print(value)
    for inner_value in value.values():
        print(inner_value)
    
# Output:
# Bronson 
# $0.05 
# Masha 
# $3.66 
# Roscoe 
# $1.14 
```
### What the loop is doing: 
* (outer loop) The `for` loop iterates over each value in the `dict_data` dictionary. Each value is a dictionary itself. 
* For each value (which is a dictionary), it prints the dictionary. 
  * Outer loop:
    * `value` is `{"name": "Bronson", "money": "$0.05"}`. 
    * The code prints `{"name": "Bronson", "money": "$0.05"}`.
    * This will carry on for each value in the `dict_data`.

* (inner loop) Inside the outer loop, another `for` loop iterates over each value in the inner dictionary. 
* For each value in the inner dictionary, it prints the value.
  * First inner loop:
    * `inner_value` is `Bronson`. 
    * The code prints `Bronson`. 
  * Second Iteration (Inner Loop):
    * `inner_value` is `$0.05`. 
    * The code prints `$0.05`. 

_____________________________________________________________________________________________________________________________

7. `Loop to print` specific values of the dictionary items inside a dictionary
* Write another for loop to loop through the dictionary `dict_data` but this time only `print out the money values`. 

Output should be:
``` python
list_data = [1, 2, 3, 4, 5] 
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}} 

for value in dict_data.values():
    print(value["money"])
# Output: 
# $0.05 
# $3.66 
# $1.14 
```
8. Loop through a list with a nested if statement 
* Write another `loop to loop` through the items in `list_data` and include a nested `(indented) if statement` inside the loop so that when it loops it checks the number/item in list: 

* if the number is less than 3, it prints 'less than 3' 
* if the number equals 3, it prints 'I found three' 
* if the number is greater than 3, it prints 'greater than 3' 

* Output should be: 

``` python
list_data = [1, 2, 3, 4, 5]

for number in list_data:
    if number < 3:                      # if number is less than (<) 3.
        print('less than 3')
    elif number == 3:                   # else if number is equal to (==) 3.
        print('I found three')
    else:
        print('greater than 3')

# Output: 
# less than 3 
# less than 3 
# I found three 
# greater than 3 
# greater than 3 
``` 
Explanation:
* Loop Through the List: The loop for `number in list_data:` goes through each item in the list one by one.
* Check Each Number: Inside the loop, the `if` statements check the value of each number:
* If the number is less than 3, it prints “less than 3”.
* If the number is exactly 3, it prints “I found three”.
* If the number is greater than 3, it prints “greater than 3”.

* This way, each number in the list is checked and the appropriate message is printed based on its value. 


