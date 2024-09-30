## Rationale 
## Consolidate control flow topic 

### The options: 
* Battle Game 
* Dice roll game 
* Interactive quiz game 
* All the games should use the CLI (not anything like the pygame library). 

## Battle game
* Make a 2 player battle game using Python.
* Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.
* If Player 2, let them pick the character/fighter they want. If CPU, assign a character/fighter randomly.
* The two Pokemon/fighters/characters need to fight.
* A winner must be declared via some sort of calculation.
* Bonus: Want to play again?
* Note: No Pygame or Turtle allowed. CLI only.

### Step-by-Step Explanation
* `Import necessary libraries`:
  * We’ll use the random library to randomly assign characters.
* `Define characters`:
  * Create a list of characters that players can choose from.
* `Character selection`:
  * Allow Player 1 to choose a character.
  * If Player 2 is a CPU, assign a character randomly; otherwise, let Player 2 choose.
* `Battle logic`:
  * Implement a simple battle logic to determine the winner.
* `Play again option`:
  * Ask if players want to play again.

```python
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
```

## Interactive Quiz Game
* This is an interactive quiz game where the user answers questions and gets a score at the end.

### Step-by-Step Explanation
* `Import necessary libraries:`
  * No additional libraries needed for this simple quiz.
* `Define questions and answers`:
  * Create a list of questions and their correct answers.
* `Quiz logic`:
  * Ask each question, check if the answer is correct, and keep track of the score.
* `End of quiz`:
  * Display the final score and ask if the user wants to play again.

```python
# Interactive quiz game.

# Define questions and answers.

questions = [           # A dictionary within a list.
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "What is 9 x 9?", "answer": "81"},
    {"question": "What is the colour of grass?", "answer": "green"}
]

def play_quiz():
    score = 0       # Somewhere to store the score.
    print("Welcome to the quiz game!")
    ready = input("Are you ready to play? (yes/no): ").lower()  # .lower() = making it lower case.
    if ready != "yes":
        return

    for q in questions:
        answer = input(q["question"] + " ")             # Only shows the question each time.
        if answer.lower() == q["answer"].lower():       # if users answer is equal to the game answer (in lowercase).
            score += 1                                  # Score goes up, everytime it matches. 

    print(f"Your final score is {score}/{len(questions)}")      # Score out of how many questions there are. 
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_quiz()

play_quiz()
```




