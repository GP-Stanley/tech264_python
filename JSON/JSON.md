# JSON
## What is JSON?
* JSON is text, written with JavaScript object notation.
* Python has a built-in package called json, which can be used to work with JSON data.
* A popular, open standard file format for storing and exchanging data.


## What does it stand for?
* JavaScript Object Notation. 

## What is it used for?
*  for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa).

## What is it written in?
* The JSON syntax is derived from JavaScript object notation syntax, but the JSON format is text only. 
* Code for reading and generating JSON data can be written in any programming language.

## Include a simple example of JSON
* a JSON object with key-value pairs, such as:
```python
{ "first_name" : "Sammy", "last_name" : "Shark", "location" : "Ocean", "online" : true, "followers" : 987 } 
```
## Advantages of using it?
* Flexibility: can support a wide range of data types.
* Easability: easy to use and understand, doesn't require additional code to interpret data.
* Support: JSON is supported by most programming languages, operating systems and browsers.
* Self-describing: easy to distinguish between data types and interpret data without prior knowledge.

## What data types can it store/use?
* string : number : JSON object : array : boolean : null.
* It CAN'T store a function : a date : undefined. 

## What is the JSON syntax for:
* used to structure data in a text-based format that is both human-readable and machine-parsable.

### Name value pairs?
* In JSON, data is written as name/value pairs. 
* A name/value pair consists of a field name (in double quotes), followed by a colon, followed by a value.
```python
"name": "John"
```
### Objects?
* JSON objects are collections of name/value pairs enclosed in curly braces {}. 
* Each name/value pair is separated by a comma. 
```python
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

### How to separate data (key/value pairs) from one another?
* name/value pairs are separated by commas. 
```python
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

### JSON arrays (these are like lists in python)?
* JSON arrays are ordered collections of values enclosed in square brackets []. 
* These values can be strings, numbers, objects, arrays, booleans, or null. 

```python
{
  "names": ["John", "Jane", "Doe"],
  "ages": [30, 25, 22]
}
```