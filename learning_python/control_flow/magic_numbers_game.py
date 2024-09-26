import random

# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# Define/assign number to a variable called magic_number
# Ask user for input
# Check if this input matches magic_number
# Let the user know if the response was correct or not
# Allow the user 5 guesses

magic_number = random.randint(1, 100)
attempts = 5

while attempts > 0:
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
        attempts -= 1
    else:
        print("Make sure you're only inputting numbers. Don't worry, that go doesn't count. ")

    print(f"You have {attempts} attempts left.")

if attempts == 0 and guess != magic_number:
    print(f"Game over! The magic number was {magic_number}.")