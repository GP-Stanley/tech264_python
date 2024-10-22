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
    ready = input("Are you ready to play? (y/n): ").lower()  # .lower() = making it lower case.
    if ready != "y":
        return

    for q in questions:
        answer = input(q["question"] + " ")             # Only shows the question each time.
        if answer.lower() == q["answer"].lower():       # if users answer is equal to the game answer (in lowercase).
            score += 1                                  # Score goes up, everytime it matches.

    print(f"Your final score is {score}/{len(questions)}")      # Score out of how many questions there are.
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "yes":
        play_quiz()

play_quiz()
