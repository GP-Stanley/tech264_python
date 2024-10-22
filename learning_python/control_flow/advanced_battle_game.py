from random import randint, choice
from time import sleep      # Pauses the program for a short period to make the game feel more natural.


# Define fighters

# Constant
FIGHTERS_NAMES = ["Elf🧝", "Ninja🥷", "Vampire🧛", "Wizard🧙‍♂️"]
ATTACK_NAMES = ["⚔️", "🪓", "🪄", "🏹"]
LIFE = 75


# Methods
def yes_no_question(question : str):
    # Prompt player with the provided question.
    while True:
        sequence_printing(f"{question} y/n: ", break_line=False)
        answer = input(f"\r{question} y/n: ")

        if answer.lower() not in ["y", "n"]:
            print_warning("⚠️ Respond only with y (yes) or n (no)")
            sleep(0.8)
            continue

        return True if answer.lower() == "y" else False

def sequence_printing(string:str, break_line = True):
    printed = ""
    for ch in string:
        printed += ch
        print(f"\r{printed}", end='')
        sleep(.02)

    if break_line:
        print()

def print_warning(warn_string, repetitions = 5, speed = 0.25):
    for i in range(0, repetitions*2):
        print(f"\r{'' if i % 2 == 0 else warn_string}", end='')
        sleep(speed)
    print()

# New Game
def new_game():
    # Start a new game. Only breaks after winning or character selection.

    fighters = []

    # Initialise the fighters.
    for i, name in enumerate(FIGHTERS_NAMES):
        fighters.append(
            {
                "id": i,
                "name": name,
                "life": LIFE,
                "attacks": [{
                    "id": ii,
                    "name": att_name,
                    "power": randint(10, 16),
                    "used": False
                } for ii, att_name in enumerate(ATTACK_NAMES)
                ]
            }
        )

    def print_fighters():
        # Print a list of available fighters.
        sequence_printing("SELECT A FIGHTER: ")

    # Get the length of longest name.
        longest_name_length = sorted([len(f.get('name')) for f in fighters])[-1]

        for fighter in fighters:
            avg_attack = sum([att.get("power") for att in fighter.get("attacks")]) / len(fighter.get("attacks"))

            # Calculate spaces to print neatly.
            spaces = longest_name_length - len(fighter.get('name'))

            #
            fighter_string = f"{fighter.get('id')}. {fighter.get('name').upper()} "
            fighter_string += " "*spaces
            fighter_string += f"|  ⚔️ Avg att: {avg_attack:.2f} - 🛡️ Life: {fighter.get('life')}"

            sequence_printing(fighter_string)

    def select_character():

        # Initialise players.
        players = []

        # P1 character selection
        p1_character = select_character()
        players.append(p1_character)
        fighters.remove(p1_character)

        # Check for player 2 or set as CPU

        is_player_2 = yes_no_question("🎮 Add player 2 to the game?")
        if is_player_2:
            players.append(select_character())
        else:
            players.append(choice(fighters))

        print('\n')
        sequence_printing(f"The fight will be between: ")
        sequence_printing(f"\t{players[0].get('name')} vs {players[1].get('name')}")
        sleep(.8)

        # Confirm start of fight
        print('\n')
        if yes_no_question("🔔 Ready to start the fight?") == False:
            return

        # Countdown
        for n in ["🕔5️⃣", "🕓4️⃣", "🕒3️⃣", "🕑2️⃣", "🕐1️⃣"]:
            print(f"\r{n}", end='')
            sleep(1)
        print()

        print_warning("🤜 FIGHT!! 🤛")


        # GAMEPLAY METHODS
        def print_life():

        def throw_dice():

        def print_attacks():

        def choose_attack():

        def reset_attacks():

        def print_player_damages(player, damage):

        # GAMEPLAY
        is_gameover = False
        round = 0

        while not is_gameover:
            round += 1

            print('-'*25)
            print(f"ROUND {round}")
            sleep(0.5)

            # Check if last round is multiple of numer of attacks, then there are no more available attacks.
            if (round - 1) % len(ATTACK_NAMES) == 0:
                reset_attacks()

            # PLAYERS TURN
            for i in range(0,len(players)):

                # Show current status
                print_life()
                sleep(0.8)

                # Set which player is attacking/defending
                current_player = i
                defending_player = 1 if i ==0 else 0
                sequence_printing(f"Its {players[current_player].get('name')} (P{current_player + 1}) turn to attack."))
                sleep(0.3)

                # If playing against CPU
                if not is_player_2 and current_player == 1:
                    sleep(0.5)
                    available_attacks = [ atts for atts in players[current_player].get("attacks") if not atts.get('used')]
                    chosen_attack = choice(available_attacks)
                    sequence_printing(f"{players[current_player].get('name')} wants to use {choose_attack.get('name')}:{chosen_attack.get('power')}")
                    sleep(0.8)

                else:
                    # Chosen attack
                    chosen_attack = choose_attack(players[current_player])
                    sequence_printing(f"{players[current_player].get('name')} wants to use {choose_attack.get('name')}:{chosen_attack.get('power')}")

                    # Roll dice
                    input("🎲 Press enter to roll dice.")

                # Set the attack to used.
                chosen_attack['used'] = True
                players[current_player]['attacks'][chosen_attack.get('id')] = chosen_attack

                # Roll the dice
                dice_result = throw_dice()
                sequence_printing(f"{players[current_player].get('name')} rolled 🎲 {dice_result}.")
                sleep(0.2)

                # Calculate attack power
                att_power = chosen_attack.get('power') * dice_result // 12
                is_power_higher = False
                sequence_printing(f"{players[current_player].get('name')} attack power {'increased' if is_power_higher else 'decreased'} and its now: {att_power} {'🎲' if is_power_higher}")

                # Show battle
                print('\n')
                sleep(0.7)
                for boom in "💥💥💥💥":
                    print(boom, end='')
                    sleep(0.7)
                print()
                sleep(0.8)
                sequence_printing(f"{players[defending_player].get('name')} was hit with a powerful attack!")
                sleep(0.8)

                # Check if defending player died
                if players[defending_player]["life"] - att_power <= 0:

                    sequence_printing(f"☠️ KILLERBLOW☠️")
                    sleep(1)
                    sequence_printing(f"{players[defending_player].get('name').upper()} IS DEAD! ")
                    sleep(1)

                    # WINNER CONGRATULATIONS
                    print("\n")
                    congrats_string = f"🎉🎊🍾 Congratulations player {current_player + 1}!! 🍾🎊🎉"
                    print("🥳🎈🎉🎊🎉💃"*(len(congrats_string)//7))
                    sequence_printing(congrats_string

                if round == 1:
                    congrats_string += f"You won after just {round} round!"
                else:
                    congrats_string += f"You won after {round} rounds!"
                sequence_printing(congrats_string)

                # Terminate
                is_gameover = True
                break

            # Change defending player's lfe
            print_player_damages(players[defending_player], att_power)
            #print(f"{players[defending_player].get('life')} --> {players[defending_player].get('life') - att_power}")
            players[defending_player]["life"] += att_power
            print("\n")
            sleep(0.8)





if __name__ == '__main__':

    play_again = True
    while play_again:
        new_game()
        print('-'*25)
        play_again = yes_no_question("Do you want to play again? (y/n)")


# A winner must be declared via some sort of calculation.













