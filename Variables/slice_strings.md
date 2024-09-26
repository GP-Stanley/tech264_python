## Slice StringsExplain: What is slicing strings?

Here is your starting code. You may need to:
- Write code to do what the comments ask for.
- Write a comment to explain what the code does.
```python
Hw = "Hello world!"
print(Hw)
```

- Find out how many characters Hw has
- Get the character in the first position in Hw
- Get the last character
- Get the 2nd last character


- Write a comment to EXPLAIN what does this do: print(Hw[2:])
- Write a comment to EXPLAIN what does this do: print(Hw[-3:])
- Write a comment to EXPLAIN what does this do: print(Hw[:5])
- Starts from the second, stops at the fifth (doesn't include it)


### What is slicing strings?
* String slicing is a technique used to extract a portion of a string.
* It allows you to create a new string from a subset of the original string by specifying a range of indices.
* This is particularly useful when you need to manipulate or analyse specific parts of a string.

#### Find out how many characters 'Hw' has.
```python
Hw = "Hello world!"
print(Hw)

length = len(Hw)                                    
print(f"{Hw} has {length} amount of characters.")
# Output: Hello world! has 12 amount of characters.
```
```python              
first_char = Hw[0]                     
print(f"'{first_char}' is the first character in {Hw}.")
# 'H' is the first character in Hello world!.
```


Get the last character in 'Hw'. Output: !
```python
last_char = Hw[-1]                     
print(f"The last character is: '{last_char}'.")
# Output: The last character is: '!'.
```
```python
# Write a comment to EXPLAIN what this does: print(Hw[2:])
print(Hw[2:])                                # This slices the string from the 3rd character to the end.
                                             # Output: "llo world!"


# Write a comment to EXPLAIN what this does: print(Hw[-3:])
print(Hw[-3:])                              # This slices the string from the 3rd last character to the end.
                                            # Output: "ld!"


# Write a comment to EXPLAIN what does this do: print(Hw[:5])
print(Hw[:5])                       # This slices the string from the beginning to the 5th character (exclusive).
                                    # Output: "Hello"


# Starts from the second, stops at the fifth (doesn't include it)
slice_example = Hw[1:5]         # This slices the string from the 2nd character to the 5th character (exclusive).
print(slice_example)            # Output: "ello"
Get the second to last character. Output: d
```python
second_last_char = Hw[-2]                           
print(f"The second-to-last character is: '{second_last_char}'.")
# Output: The second-to-last character is: 'd'.
```

Write a comment to EXPLAIN what this does: _print(Hw[2:])_
* This slices the string from the 3rd character to the end. 
* Output: "llo world!"


Write a comment to EXPLAIN what this does: _print(Hw[-3:])_
* This slices the string from the 3rd last character to the end.
* Output: "ld!"


Write a comment to EXPLAIN what does this do: print(Hw[:5])
* This slices the string from the beginning to the 5th character (exclusive).
* Output: "Hello"


Starts from the second, stops at the fifth (doesn't include it)
* This slices the string from the 2nd character to the 5th character (exclusive).
* Output: "ello"
```python
slice_example = Hw[1:5]
print(slice_example)
# Output: ello
```          