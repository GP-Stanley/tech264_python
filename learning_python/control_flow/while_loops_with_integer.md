## Using `while loops` with an integer

* Create a new file named 'while_loops.py' or similar. 
* Initialise x with the value of 0 
* Create a while statement so that it loops while x is less than 10. Everytime it loops it should: 
* Print the value of x to the screen in an f-string 
* Increment (add 1 to x) 

Running this code should produce: 

``` python
x = 0                                   # initialise x to the value of 0.
while x < 10:                           # while x is less than (<) 10.
    print(f"The value of x is: {x}")
    x += 1                              # x is increased by 1 (x += 1) each time.
                                        # the while loop repeats with the new value of x.
# Output:
# print x -> 0 
# print x -> 1 
# print x -> 2 
# print x -> 3 
# print x -> 4 
# print x -> 5 
# print x -> 6 
# print x -> 7 
# print x -> 8 
# print x -> 9 
``` 
* Once your code works, find out what happens when you run the code if you comment out the first line which initialises 'x'. 
* Write a brief comment on the line before the code which increments x to explain what would happen if you don't increment x. 
* Copy and paste your working `while loop` underneath the `while loop`. Modify the second copy of the 'while loop' so that it breaks out of the loop when x equals 4. 
* If you comment out the initialisation of x, the code will raise a `NameError` because x is not defined.

``` python
x = 0
while x < 10:
    print(f"The value of x is: {x}")
    if x == 4:                              # if statement checks if x is equal (==) to 4.
        break                                   # if the condition is True, the break statement will stop the while loop.
    x += 1                                  # if x is not equal to 4, x is increased by 1 (x += 1).
                                            # the loop will repeat with the new value of x but stop (<10).
# Output: 
# print x -> 0 
# print x -> 1 
# print x -> 2 
# print x -> 3 
# print x -> 4 
``` 




