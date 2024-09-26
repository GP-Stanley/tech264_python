## Magic Numbers Game!!

> As a `<type of user>`, I want `<goal>`, so that `<reason>`

### User story 1 
* As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not. 
* Define/assign number to a variable called magic_number 
* Ask user for input 
* Check if this input matches magic_number 
* Let the user know if the response was correct or not 
* Allow the user 5 guesses 

```python
magic_number = 33
attempts = 4

for attempts in range(attempts):
    guess = input("Can you guess the magic number? Have a guess: ")
    if guess.isdigit():
        guess = int(guess)
    if guess == magic_number:
        print("You must psychic!")
    if guess != magic_number:
        print("You're definitely NOT psychic!")
```
### WITH A `FOR LOOP`, `ITERATIONS ARE FIXED`: THIS IS WHY IT DIDN'T WORK IN LEVEL 2 & 3.

## Level 2
Challenge yourself to get from Level 1 to Level 2 in 10 min. 

### User story 2 
* As a user, I want to be able to guess a number and know if I need to go higher or lower. 
### User story 3 
* As a user, I don't want my guesses wasted if I enter something accidently as my guess which are not digits.
### User story 4 
* As a user, after each guess, I would like to know how many guesses I have left.
```python
magic_number = 33
attempts = 5

while attempts > 0:                         # changed to `while loop` because `for loop` didn't work.
    guess = input("Can you guess the magic number? Have a guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess < magic_number:
            print("Too low!")
        if guess > magic_number:
            print("Too High!")
        if guess == magic_number:
            print("Looks like we've found a game you're good at!")
            break
        attempts -= 1                         # this lowers the guesses if a number is submitted. 
    else:
        print("Make sure you're only inputting numbers. Don't worry, that go doesn't count. ")

    print(f"You have {attempts} attempts left.")            # how many guesses you have left.

if attempts == 0 and guess != magic_number:              
    print(f"Game over! You lose!")
```
## Level 3
Challenge yourself to get from Level 2 to Level 3 in 10 min 


### User story 5 
* As a user, I would like the magic to be randomly generated each time I play so it is more fun. 

### User story 6 
* As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly and I've used up all my tries. 

**Hint**: Use the Python library random to generate a random number rather than assigning one 
 ```python
magic_number = random.randint(1, 100)           # random.randint() lets you randomise a number between 1 - 100.
attempts = 5

while attempts > 0:                             #  The while loop runs as long as attempts is greater than 0.
    guess = input("Can you guess the magic number? It's between 1 and 100. Have a guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess < magic_number:
            print("Too low!")
        if guess > magic_number:
            print("Too High!")
        if guess == magic_number:
            print("Looks like we've found a game you're good at!")
            break
        attempts -= 1                           #  If the guess is incorrect, attempts is decreased by 1.
    else:
        print("Make sure you're only inputting numbers. Don't worry, that go doesn't count. ")

    print(f"You have {attempts} attempts left.")                # Tells you how many attempts you have left.

if attempts == 0 and guess != magic_number:
    print(f"Game over! The magic number was {magic_number}.")       # Tells you the magic number. 
```

