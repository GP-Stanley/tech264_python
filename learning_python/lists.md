# Lists

* List items are ordered, changeable, and allow duplicate values. 
* List items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.

## Ordered
* When we say that lists are ordered, it means that the items have a `defined order`, and that `order will not change`. 
* If you add new items to a list, the `new items will be placed at the end` of the list.

## Changeable
* The list is changeable, meaning that we can `change`, `add`, and `remove` items in a list `after it has been created`.

### List Methods
| Method    | Description                                                        |
|-----------|--------------------------------------------------------------------|
| append()  | Adds an element at the end of the list                             |
| clear()   | Removes all the elements from the list                             |
| copy()    | Returns a copy of the list                                         |
| count()   | Returns the number of elements with the specified value            |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list |
| index()   | Returns the index of the first element with the specified value    |
| insert()  | Adds an element at the specified position                          |
| pop()     | Removes the element at the specified position                      |
| remove()  | Removes the item with the specified value                          |
| reverse() | Reverses the order of the list                                     |
| sort()    | Sorts the list                                                     |


### Duplicate example
```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)
# Output: ['apple', 'banana', 'cherry', 'apple', 'cherry']
```

## List Length
* To determine how many items a list has, use the len() function
```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# Output: 3
```

## List Items - Data Types
* List items can be of any data type.
```python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
# Output:
# (['apple', 'banana', 'cherry'])
# ([1, 5, 7, 9, 3])
# ([True, False, False])
```

* A list can contain different data types: A list with strings, integers and boolean values.
```python
list1 = ["abc", 34, True, 40, "male"]

print(list1)
# Output: ['abc', 34, True, 40, 'male']
```

## type()
* From Python's perspective, lists are defined as objects with the data type 'list'.
```python
mylist = ["apple", "banana", "cherry"]

print(type(mylist))
# Output: <class 'list'>
```

## The list() Constructor
* It is also possible to use the `list()` constructor when creating a new list.
```python
thislist = list(("apple", "banana", "cherry"))
print(thislist)
# Output: ['apple', 'banana', 'cherry']
```

## Python Collections (Arrays)
There are four collection data types in the Python programming language:
* `List` is a collection which is `ordered and changeable`. Allows duplicate members.
* `Tuple` is a collection which is `ordered and unchangeable`. Allows duplicate members.
* `Set` is a collection which is `unordered, unchangeable*, and unindexed`. No duplicate members.
  * *Set items are `unchangeable`, but you can `remove and/or add items` whenever you like.
* `Dictionary` is a collection which is `ordered** and changeable`. No duplicate members.
  * **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

## Access Items
* List items are `indexed` and you can access them by `referring to the index number`.
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Output: banana
```

## Negative Indexing
* Negative indexing means start from the end.
  * `-1` refers to the `last item`, -2 refers to the second last item etc.
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# Output: cherry
```

## Range of Indexes
* You can specify a `range` of indexes by specifying `where to start` and `where to end` the range. 
* When specifying a range, the return value will be a new list with the specified items.
```python
# Return the third, fourth, and fifth item.
# Note: The search will start at index 2 (included) and end at index 5 (not included).

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])                        #This will return the items from position 2 to 5.

# Remember that the first item is position 0,
# and note that the item in position 5 is NOT included : aka: 2, 3, 4.

# Output: ['cherry', 'orange', 'kiwi']
```
```python
# By leaving out the start value, the range will start at the first item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])         # This will return the items from index 0 to index 4 : aka, 0, 1, 2, 3.

# Remember that index 0 is the first item, and index 4 is the fifth item.
# Remember that the item in index 4 is NOT included.

# Output: ['apple', 'banana', 'cherry', 'orange']
```
```python
# By leaving out the end value, the range will go on to the end of the list.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])                 # This will return the items from index 2 to the end.

# Remember that index 0 is the first item, and index 2 is the third.

# Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']
```

## Range of Negative Indexes
* Specify negative indexes if you want to `start the search from the end` of the list.
```python
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])          # Output: ['orange', 'kiwi', 'melon']

# Negative indexing means starting from the end of the list.

# This example returns the items from index -4 (included) to index -1 (excluded)

# Remember that the last item has the index -1.
```

## Check if Item Exists
* To determine if a specified item is present in a list use the `in` keyword.
```python
# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
# Output: Yes, 'apple' is in the fruits list.
```

# Change List Items

## Change value item
* To change the value of a specific item, refer to the index number.
```python
# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)             # Output: ['apple', 'blackcurrant', 'cherry']
```

## Change a Range of Item Values
* To `change the value of items` within a specific range, 
  * `define a list` with the `new values`, and 
  * `refer to the range of index numbers` where you want to `insert the new values`.
```python
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)         # Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```
* If you `insert more items than you replace`, the `new items will be inserted where you specified`, and the `remaining items will move accordingly`.
* The length of the list will change when the number of items inserted does not match the number of items replaced.
```python
# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)     # Output: ['apple', 'blackcurrant', 'watermelon', 'cherry']
```
* If you `insert less` items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.
```python
# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]

print(thislist)         # Output: ['apple', 'watermelon']
```

## Insert Items
* To insert a new list item, without replacing any of the existing values, we can use the `insert()` method. 
* The `insert()` method `inserts an item at the specified index`.
```python
# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")

print(thislist)             # Output: ['apple', 'banana', 'watermelon', 'cherry']
```

# Add list items

## Append Items
* To add an item to the end of the list, use the `append()` method.
```python
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   

print(thislist)         # Output: ['apple', 'banana', 'cherry', 'orange']
```

## Insert Items
* To insert a list item at a specified index, use the `insert()` method. 
* The `insert()` method `inserts an item at the specified index`.
```python
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")

print(thislist)         # Output: ['apple', 'orange', 'banana', 'cherry']
```

## Extend List
* To combine elements from another list to the current list, use the `extend()` method.
* The elements will be added to the end of the list.
```python
# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)         # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

## Add Any Iterable
* The `extend()` method does not have to append `lists`.
* You can `add any iterable object` (`tuples`, `sets`, `dictionaries` etc.).
* The elements will be added to the end of the list.
```python
# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist)             # Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']
```

# Remove List Items
## Remove Specified Item
* The `remove()` method removes the specified item.
```python
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")

print(thislist)         # Output: ['apple', 'cherry']
```
* If there are more than one item with the specified value, the `remove()` method `removes the first occurrence`.
```python
# Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")

print(thislist)         # Output: ['apple', 'cherry', 'banana', 'kiwi']
```

## Remove Specified Index
* The `pop()` method `removes the specified index`.
* If you `do not specify` the index, the `pop()` method `removes the last item`.
```python
# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
# thislist.pop() --> this removes the last item on the list. 

print(thislist)         # Output: ['apple', 'cherry']
```

## `del` keyword
* The del keyword also removes the specified index, (`del thislist[0]`).
* The del keyword can also delete the list completely, (`del thislist`).


## Clear the List
* The `clear()` method empties the list. 
* The list still remains, but it has no content.
```python
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()

print(thislist)         # Output: []
```

# Loop Lists
## Loop through a list
* You can loop through the list items by using a `for` loop.
```python
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Output:
# apple
# banana
# cherry
```

## Loop through the index numbers
* You can also loop through the list items by referring to their index number. 
* Use the `range()` and `len()` functions to create a suitable iterable.
```python
# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Output:
# apple
# banana
# cherry
```

## Using a While Loop
* You can `loop through the list` items by using a while loop. 
* Use the `len()` function to `determine the length` of the list, then start at 0 and loop your way through the list items by referring to their indexes. 
* Remember to `increase the index by 1 after each iteration`.
```python
# Print all items, using a while loop to go through all the index numbers.

thislist = ["apple", "banana", "cherry"]
i = 0           # We set a variable i to 0. This variable will be used to keep track of our position in the list.
while i < len(thislist):        # while loop that will continue to run as long as i is less than the length of thislist. The len(thislist) function returns the number of items in the list, which is 3 in this case.
  print(thislist[i])            # print(thislist[i]) to print the item at the current position i in the list. The first time the loop runs, i is 0, so it prints "apple". The next time, i is 1, so it prints "banana", and so on.
  i = i + 1         # After printing the current item, we increase the value of i by 1. This moves us to the next position in the list.

# Output:
# apple
# banana
# cherry
```

## Looping Using List Comprehension
* List Comprehension offers the shortest syntax for looping through lists.
```python
# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Output:
# apple
# banana
# cherry
```

## Use the slice Operator
* You can also make a copy of a list by using the `:` (slice) operator.
```python
# Make a copy of a list with the `:` operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)           # Output: ['apple', 'banana', 'cherry']
```













