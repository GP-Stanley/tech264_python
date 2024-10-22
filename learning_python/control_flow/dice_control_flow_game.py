# Dice game

import random           # import necessary libraries.

def roll_dice():
    return random.randint(1, 6)         # Random number between 1 and 6 (like a dice).

def play_dice_game():           # Function to play the dice game.
    user_score = 0              # Where we store the score.
    cpu_score = 0
    user_name = input("Enter your name: ")

    print("Welcome to the dice game!")
    ready = input("Are you ready to play? (y/n): ").lower()     # Keeps user answer lowercase.
    if ready != "yes":
        return

    while user_score < 30 and cpu_score < 30:           # while the score is less than 30.
        user_roll = roll_dice()
        cpu_roll = roll_dice()
        print(f"{user_name} rolled {user_roll}")
        print(f"CPU rolled {cpu_roll}")

        user_score += user_roll         # user score is equal to their roll.
        cpu_score += cpu_roll

        print(f"Scores -> {user_name}: {user_score}, CPU: {cpu_score}")

    if user_score >= 30:            # score is greater than/ equal to 30 - game is finished.
        print(f"{user_name} wins!")
    else:
        print("CPU wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_dice_game()

play_dice_game()






