# Dictionaries

## Dictionary Methods
| Method       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `clear()`      | Removes all the elements from the dictionary                                |
| `copy()`       | Returns a copy of the dictionary                                            |
| `fromkeys()`   | Returns a dictionary with the specified keys and value                      |
| `get()`        | Returns the value of the specified key                                      |
| `items()`      | Returns a list containing a tuple for each key value pair                   |
| `keys()`       | Returns a list containing the dictionary's keys                             |
| `pop()`        | Removes the element with the specified key                                  |
| `popitem()`    | Removes the last inserted key-value pair                                    |
| `setdefault()` | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| `update()`     | Updates the dictionary with the specified key-value pairs                   |
| `values()`     | Returns a list of all the values in the dictionary                           |


```python
# Example:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

## Dictionary
* Dictionaries are used to store data values in `key:value pairs`. 
* A dictionary is a collection which is `ordered`, `changeable` and `do not allow duplicates`.
* When we say that dictionaries are `ordered`, it means that the items have a `defined order`, and that order will not change. 
* Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
* Dictionaries are `changeable`, meaning that we can `change`, `add` or `remove items` after the dictionary has been created.
* Dictionaries cannot have two items with the same key. `Duplicate` values will `overwrite existing values`.
* Dictionaries are written with curly brackets `{}`, and have `keys` and `values`.

## Dictionary Length
* To determine how many items a dictionary has, use the `len()` function.
```python
# Example
Print the number of items in the dictionary:
print(len(thisdict))
```

## Data Types
* The values in dictionary items can be of `any data type`.
```python
# String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)     # Output: {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}
print(type(thisdict))           # Output: <class 'dict'>
```

## Accessing Items
* You can access the items of a dictionary by referring to its key name, inside square brackets `[]`.
```python
# Get the value of the "model" key:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]           # x = thisdict.get("model") : this also does the same thing.
print(x)            # Output: Mustang
```

## Get Keys
* The `keys()` method will `return a list of all the keys` in the dictionary.
```python
# Get a list of the keys:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)            # Output: dict_keys(['brand', 'model', 'year'])
```

* The list of the keys is a _view_ of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
```python
# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()      # used to get a view object that displays a list of all the keys in the dictionary. Initially, x will contain dict_keys(['brand', 'model', 'year']).

print(x)            # before the change

car["color"] = "white"      # add a new key-value pair to the dictionary: "color": "white". 

print(x)            # after the change

# Output:
# dict_keys(['brand', 'model', 'year'])
# dict_keys(['brand', 'model', 'year', 'color'])
```

## Get Values
* The `values()` method will `return a list of all the values` in the dictionary.
```python
# Get a list of the values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)            # Output: dict_values(['Ford', 'Mustang', 1964])
```

* The list of the values is a _view_ of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
```python
# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)            # before the change

car["year"] = 2020

print(x)            # after the change

# Output:
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 2020])
```

### Get Items
* The `items()` method will return each item in a dictionary, as tuples in a list.
```python
# Get a list of the key:value pairs:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)            # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

## Check if Key Exists
* To determine if a specified key is present in a dictionary use the in keyword.
```python
# Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Output: Yes, 'model' is one of the keys in the thisdict dictionary.
```

## Change Values
* You can change the value of a specific item by `referring to its key name`.
```python
# Change the "year" to 2018:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)         # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
```

## Update Dictionary
* The `update()` method will update the dictionary with the items from the given argument. 
* The argument must be a dictionary, or an iterable object with `key:value pairs`.
```python
# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)         # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

## Adding Items
* Adding an item to the dictionary is done by using a new index key and assigning a value to it.
```python
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)         # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
```

## Update Dictionary
* The `update()` method will update the dictionary with the items from a given argument. `If the item does not exist, the item will be added`.
* The argument must be a dictionary, or an iterable object with key:value pairs.
```python
# Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)         # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
```

# Remove Dictionary Items

## Removing Items
* There are several methods to remove items from a dictionary.

```python
# The pop() method removes the item with the specified key name:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)         # Output: {'brand': 'Ford', 'year': 1964}
```
```python
# The popitem() method removes the last inserted item:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)         # Output: {'brand': 'Ford', 'model': 'Mustang'}
```

# Loop Dictionaries

## Loop Through a Dictionary
* You can loop through a dictionary by using a `for` loop. 
* When looping through a dictionary, the `return value are the keys` of the dictionary, but there are methods to return the values as well.
```python
# Print all key names in the dictionary, one by one:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# Output:
# brand
# model
# year
```
```python
# Print all values in the dictionary, one by one:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

# Output:
# Ford
# Mustang
# 1964
```
```python
# You can also use the values() method to return values of a dictionary: 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

# Output:
# Ford
# Mustang
# 1964
```

* `Loop through both keys and values`, by using the `items()` method.
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

# Output:
# brand Ford
# model Mustang
# year 1964
```

# Nested Dictionaries
* A `dictionary can contain dictionaries`, this is called `nested dictionaries`.
```python
# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)         # Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

```

### Or, if you want to add three dictionaries into a new dictionary:
```python
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)         # {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

```

## Access Items in Nested Dictionaries
* To access items from a nested dictionary, you `use the name of the dictionaries`, `starting with the outer dictionary`.

```python
# Print the name of child 2:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])           # Output: Tobias
```

## Loop Through Nested Dictionaries
* You can loop through a dictionary by using the `items()` method like this.
```python
# Loop through the keys and values of all nested dictionaries:

for x, obj in myfamily.items():         # x will be the key, and obj will be the value (which is another dictionary).
    print(x)
    
    for y in obj:           # obj is a dictionary (the value from the outer dictionary) : y will be the key of this inner dictionary.
        print(y + ':', obj[y])      # This prints the key (y) and its corresponding value (obj[y]) from the inner dictionary.

# Output:
# child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011
```





