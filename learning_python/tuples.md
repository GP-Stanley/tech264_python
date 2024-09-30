# Tuples
* Tuples are used to `store multiple items in a single variable`. 
* Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. 
* A tuple is a collection which is `ordered and unchangeable`. 
* Tuples are written with `round brackets`.
* Tuple items can be of `any data type`: `string`, `int`, `boolean`.
  * A tuple can `contain different data types`.

## Tuple Methods
| Method  | Description                                                                 |
|---------|-----------------------------------------------------------------------------|
| count() | Returns the number of times a specified value occurs in a tuple             |
| index() | Searches the tuple for a specified value and returns the position of where it was found |


## Tuple Items
* Tuple items are `ordered, unchangeable`, and `allow duplicate` values. 
* Tuple items are `indexed`, the first item has index [0], the second item has index [1] etc.

## Ordered
* When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

## Unchangeable
* Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

## Allow Duplicates
* Since tuples are indexed, they can have items with the same value.
```python
# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)            # Output: ("apple", "banana", "cherry", "apple", "cherry")
```

## Tuple Length
* To determine how many items a tuple has, use the `len()` function.
```python
# Print the number of items in the tuple:

thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))           # Output: 3
```

## Create Tuple With One Item
* To create a tuple with only one item, you have to `add a comma after the item`, otherwise Python will not recognize it as a tuple.

## The tuple() Constructor
 It is also possible to use the `tuple()` constructor to make a tuple.
```python
# Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry"))            # Note the double brackets.
print(thistuple)            # Output: ("apple", "banana", "cherry")
```

## Access Tuple Items
* You can access tuple items by `referring to the index number`, inside square brackets `[]`.
```python
# Print the second item in the tuple.

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])         # Output: banana
```

## Negative Indexing
* `Negative indexing` means `start from the end`. 
* `-1` refers to the `last item`, `-2` refers to the `second last item` etc.
```python
# Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])            # Output: cherry
```

## Range of Indexes
* You can specify a range of indexes by `specifying where to start and where to end` the range. 
* When specifying a range, the `return value` will be `a new tuple with the specified items`.
```python
# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])           # This will return the items from position 2 to 5 : Output: ('cherry', 'orange', 'kiwi')

# Remember that the first item is position 0,
# and note that the item in position 5 is NOT included.
# Note: The search will start at index 2 (included) and end at index 5 (not included).
```

* By leaving out the start value, the range will start at the first item.
```python
# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[:4])            # Output: ('apple', 'banana', 'cherry', 'orange')
```

* By leaving out the end value, the range will go on to the end of the tuple.
```python
# This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:])            # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')
```

## Range of Negative Indexes
* Specify negative indexes if you want to start the search from the end of the tuple.
```python
# This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])         # Negative indexing means starting from the end of the tuple: Output: ('orange', 'kiwi', 'melon')

# This example returns the items from index -4 (included) to index -1 (excluded)
# Remember that the last item has the index -1.
```

## Check if Item Exists
* To determine if a `specified item is present` in a tuple use the in keyword.
```python
# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")          # Output: Yes, 'apple' is in the fruits tuple.
```


