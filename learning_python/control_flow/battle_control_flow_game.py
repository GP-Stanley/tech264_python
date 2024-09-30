# Battle game

import random

# Define characters.
characters = ["Mum", "Dad", "Little Bro", "Big Sis"]

# Character selection.
def choose_character(player):
    if player == "CPU":         # If the character is a CPU, selection is random.
        return random.choice(characters)
    else:
        print(f"Choose your character, {player}: ")
        for i, char in enumerate(characters):
            print(f"{i + 1}. {char}")       # Output: (e.g.) 1. Mum, 2. Dad, etc.
        choice = int(input("Enter the number of your choice: ")) - 1    # '-1' picking the right one from the list.
        return characters[choice]

def battle(player1, char1, player2, char2):     # when a player choses their character, outcome will be random.
    print(f"{player1} ({char1}) vs {player2} ({char2})")
    winner = random.choice([player1, player2])
    print(f"The winner is {winner}!!")

def play_game():
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name or type 'CPU' for computer: ")

    char1 = choose_character(player1)           # Using choose_character function.
    char2 = choose_character(player2)

    battle(player1, char1, player2, char2)      # Using def battle function.

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()

play_game()


