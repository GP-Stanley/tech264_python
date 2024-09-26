#### Starting code:
```python
bad_string = 'I said 'Wow!''
print(bad_string)
```
* Why does this fail?
* Find 3 ways to make this string assignment work
* Condition: The Wow! must be surrounded in quotes when it prints to the screen.
* Explain: What is best practice when deciding what quotes to use around strings in Python?

### Escape Character
The backslash is used to introduce escape sequences, which represent characters that are difficult to include directly in a string. Common escape sequences include:
* `\n`: Newline
* `\t`: Tab
* `\\`: Backslash
* `\'`: Single quote
* `\"`: Double quote

Why does the starting code fail?
* Because it uses single quotes to close the string and also within the string ('Wow!').


Using double quotes and single quotes inside the string.
```python
bad_string = "I said 'Wow!'"
print(bad_string)                                   
```
> Output: I said 'Wow!'

The backslash separates the single quotes from the string itself.
```python
bad_string = "I said \'Wow!\'"
print(bad_string)                                   
```
> Output: I said 'Wow!'

Separated quotes.
```python
bad_string = 'I said \"Wow!\"'
print(bad_string)                                   
```
> Output: I said "Wow!"