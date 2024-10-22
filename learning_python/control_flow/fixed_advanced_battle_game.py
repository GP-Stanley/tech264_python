from random import randint, choice
from time import sleep

# Constants
FIGHTERS_NAMES = ["Elf🧝", "Ninja🥷", "Vampire🧛", "Wizard🧙‍♂️"]
ATTACK_NAMES = ["⚔️", "🪓", "🪄", "🏹"]
LIFE = 75


# Methods
def yes_no_question(question: str):
    while True:
        sequence_printing(f"{question} y/n: ", break_line=False)
        answer = input().lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print_warning("⚠️ Respond only with y (yes) or n (no)")
            sleep(0.8)


def sequence_printing(string: str, break_line=True):
    printed = ""
    for ch in string:
        printed += ch
        print(f"\r{printed}", end='')
        sleep(0.02)

    if break_line:
        print()


def print_warning(warn_string, repetitions=5, speed=0.25):
    for i in range(0, repetitions * 2):
        print(f"\r{'' if i % 2 == 0 else warn_string}", end='')
        sleep(speed)
    print()


def new_game():
    # Start a new game
    fighters = []

    # Initialize the fighters
    for i, name in enumerate(FIGHTERS_NAMES):
        fighters.append({
            "id": i,
            "name": name,
            "life": LIFE,
            "attacks": [{
                "id": ii,
                "name": att_name,
                "power": randint(10, 16),
                "used": False
            } for ii, att_name in enumerate(ATTACK_NAMES)]
        })

    def print_fighters():
        # Print a list of available fighters.
        sequence_printing("SELECT A FIGHTER:")
        longest_name_length = max(len(f.get('name')) for f in fighters)

        for fighter in fighters:
            avg_attack = sum([att.get("power") for att in fighter.get("attacks")]) / len(fighter.get("attacks"))
            spaces = longest_name_length - len(fighter.get('name'))
            fighter_string = f"{fighter.get('id')}. {fighter.get('name').upper()} "
            fighter_string += " " * spaces
            fighter_string += f"| ⚔️ Avg att: {avg_attack:.2f} - 🛡️ Life: {fighter.get('life')}"
            sequence_printing(fighter_string)

    def select_character():
        print_fighters()
        while True:
            try:
                choice = int(input("\nChoose your fighter by entering the number: "))
                if 0 <= choice < len(fighters):
                    return fighters.pop(choice)  # Select the fighter and remove them from the list
                else:
                    print_warning("⚠️ Invalid choice. Choose a valid fighter number.")
            except ValueError:
                print_warning("⚠️ Enter a valid number.")

    players = []
    players.append(select_character())  # P1 selects character
    is_player_2 = yes_no_question("🎮 Add player 2 to the game?")

    if is_player_2:
        players.append(select_character())  # P2 selects character
    else:
        players.append(choice(fighters))  # CPU selects random fighter

    sequence_printing(f"The fight will be between {players[0]['name']} and {players[1]['name']}!")
    if not yes_no_question("🔔 Ready to start the fight?"):
        return

    # Countdown to fight
    for n in ["🕔5️⃣", "🕓4️⃣", "🕒3️⃣", "🕑2️⃣", "🕐1️⃣"]:
        print(f"\r{n}", end='')
        sleep(1)
    print_warning("🤜 FIGHT!! 🤛")

    def throw_dice():
        return randint(1, 12)

    def print_life():
        for i, player in enumerate(players):
            sequence_printing(f"Player {i + 1} - {player['name']} 🛡️ Life: {player['life']}")

    def reset_attacks():
        for player in players:
            for attack in player['attacks']:
                attack['used'] = False

    is_gameover = False
    round = 0

    while not is_gameover:
        round += 1
        sequence_printing(f"ROUND {round}")
        if (round - 1) % len(ATTACK_NAMES) == 0:
            reset_attacks()

        for i in range(2):  # Loop over both players
            print_life()

            current_player = players[i]
            defending_player = players[1 - i]
            sequence_printing(f"It's {current_player['name']}'s turn to attack!")

            if not is_player_2 and i == 1:  # If CPU
                available_attacks = [att for att in current_player['attacks'] if not att['used']]
                chosen_attack = choice(available_attacks)
            else:
                chosen_attack = choice([att for att in current_player['attacks'] if not att['used']])  # Use random attack for now
            chosen_attack['used'] = True
            dice_result = throw_dice()
            att_power = chosen_attack['power'] * dice_result // 12
            defending_player['life'] -= att_power  # Correct damage calculation

            print_warning(f"{defending_player['name']} takes {att_power} damage!")

            if defending_player['life'] <= 0:
                sequence_printing(f"{defending_player['name']} is dead! 🎉")
                sequence_printing(f"Player {i + 1} wins!")
                is_gameover = True
                break

if __name__ == '__main__':
    while yes_no_question("Do you want to play again? (y/n)"):
        new_game()
