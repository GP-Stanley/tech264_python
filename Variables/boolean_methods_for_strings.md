## Boolean Methods for Strings
### Task:
* Find out what is needed using the comments as a guide.
* Each of the methods used below should return a boolean (True or False only).
* You are not allowed to use any 'if' statements.
* Find out if 'hi' is made up of letters only (use one of the strings methods). - Print the boolean to the screen.


Code to get you started:

```python
hi = "Hello World!"
```

```python
is_letters_only = hi.isalpha()
print(is_letters_only)   
```           
> Outcome: False (it contains a space)

Find out if 'hi' is made up only of lowercase letters (use one of the strings methods) - print the boolean to the screen.

```python
is_lowercase_only = hi.islower()
print(is_lowercase_only)
```            
> Outcome: False (contains uppercase letters)

Find out if 'hi' is made up only of uppercase letters (use one of the strings methods) - print the boolean to the screen.

```python
is_upper_case = hi.isupper()
print(is_upper_case)     
```           
> Outcome: False (contains lowercase letters)

Find out if 'hi' ends with an exclamation mark (use one of the strings methods) - print the boolean to the screen.

```python
ends_with_exclamation = hi.endswith("!")
print(ends_with_exclamation)  
```      
> Outcome: True (ends with exclamation mark)

Find out if 'hi' starts with a capital "h" (use one of the strings methods) - print the boolean to the screen.

```python
starts_with_capital_h = hi.startswith("H")
print(starts_with_capital_h)    
```
> Outcome: True (contains capital "H")

isalnum() Returns true if string has at least 1 character and all characters  are ALPHANUMERIC and false otherwise.

```python
is_alphanumeric = hi.isalnum()
print(is_alphanumeric)  
```            

> Outcome: False (contains no digits)

isalpha() Returns true if string has at least 1 character and all characters  are ALPHABETIC and false otherwise.

```python
is_alphabetic = hi.isalpha()
print(is_alphabetic)   
```             

> Outcome: False (contains spaces)