# Task:
# API documentation: PokéAPI (pokeapi.co)
# Recommended: Understand the Pokemon lookup program first (code below) to fully understand accessing data from the API.
# The Pokémon data MUST come from the PokeApi
# Get random Pokémon for at least the CPU (Player can be chosen or random)
# Pokémon should fight and a winner should be declared in some way
# No Pygame. Focus on interacting with the API.
# Be as creative as you like after this. Can you incorporate different abilities/stats etc.?
# Try and work collaboratively on the one repo using Git
# To deliver: Give it your best shot! Share your code (message your Ramon + Luke directly, NOT a message in the main chat) by COB (17:00)


import requests     # Allows the program to make HTTP requests to access the Pokémon API.
import json         # Used to handle JSON data, which is the format the API returns.
from random import choice, randint      # Pick random moves and Pokémon. choice picks a random item from a list, and randint generates a random integer within a range (attack stats).
from time import sleep      # Pauses the program for a short period to make the game feel more natural.

# Constants (in capitals to differentiate)
LIFE = 100  # a constant that sets the initial health points (HP) for each Pokémon in the battle.

# Get the list of Pokémon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'      # The endpoint for fetching a list of Pokémon from PokéAPI.
response = requests.get(url)        # Sends a GET request to the API to retrieve data.
pokemon_list = json.loads(response.text)['results']

# json.loads(response.text): Converts the response (which is in JSON format) into a Python dictionary.
# pokemon_list: Extracts the list of Pokémon names and URLs from the API response.

# Display all Pokémon names and their IDs
for pokemon in pokemon_list:        # Loops through each Pokémon in pokemon_list.
    pokemon_id = pokemon['url'].split('/')[-2]  # Extract Pokémon ID from URL
    print(f"{pokemon_id}. {pokemon['name']}")  # Print Pokémon ID and name

# Ask the user to choose a Pokémon by entering its name (case-insensitive due to .lower()).
user_choice = input('Enter your Pokémon: ').lower()


# Function to initialise a Pokémon (get its data from the API)
def init_pokemon(pokemon_id: str) -> dict:      # init_pokemon(): A function that initializes a Pokémon's attributes (ID, name, life points, moves) from the API using its ID.
    pokemon = {'life': LIFE}  # A dictionary pokemon is created with the initial life points set to LIFE (100).

    # Fetch Pokémon data from the API using the Pokémon ID
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    pokemon_data = json.loads(response.text)    # Sends a request to the API to get the data for the specific Pokémon (using the provided pokemon_id).

    # Store relevant Pokémon data and name in the pokemon dictionary.
    pokemon['id'] = pokemon_data['id']  # Pokémon ID
    pokemon['name'] = pokemon_data['name']  # Pokémon name

    # Format height and weight (API gives these in decimetres and hectograms)
    # Converts the Pokémon's height (decimeters) and weight (hectograms) to meters and kilograms,
    # storing them in the pokemon dictionary.
    height = pokemon_data['height'] / 10  # Convert height to meters
    weight = pokemon_data['weight'] / 10  # Convert weight to kilograms
    pokemon['height'] = height
    pokemon['weight'] = weight

    # Randomly choose 4 unique attacks (moves) for the Pokémon's available moves.
    attacks = []    # attacks is a list of dictionaries containing the move's name, URL, a random power between 15 and 20, and a flag (used) to track if the move has been used.
    while len(attacks) < 4:
        chosen_att = choice(pokemon_data['moves'])  # Pick a random move
        if chosen_att['move']['url'] not in [att['url'] for att in attacks]:
            # Add the move to the list if it's not already there
            attacks.append({
                'name': chosen_att['move']['name'],  # Move name
                'url': chosen_att['move']['url'],  # Move URL
                'power': randint(15, 20),  # Random power between 15 and 20
                'used': False  # Track if the move was used
            })
    pokemon['attacks'] = attacks  # Store the selected attacks for the Pokémon
    return pokemon  # The initialised pokemon dictionary with life, name, ID, height, weight, and attacks is returned.


# Function to print the life status of both players
def print_life():       # This function prints the current life of both Pokémon in the game, showing how much life each player has left.
    '''Prints the current life of each player'''
    string = f"{players[0].get('name')} - {players[0].get('life')}/{LIFE} 🛡️\t"
    string += f" 🛡️ {players[1].get('life')}/{LIFE} - {players[1].get('name')}\n"
    print(string)


# Initialise players
players = [         # players is a list containing two Pokémon.
    init_pokemon(user_choice),  # User's chosen Pokémon
    init_pokemon(str(randint(1, 200)))  # Random Pokémon for the CPU (from first 200 Pokémon)
]

# Mini gameplay loop
is_gameover = False  # Flag to track if the game has ended.
round = 0  # Track the number of rounds

while not is_gameover:      # The main game loop continues until a player loses.
    round += 1      # In each iteration, the round number increments, the status is printed, and the game pauses briefly.
    print('_' * 25)
    print(f"ROUND {round}")
    sleep(0.5)

    # Print current life of both players
    print_life()

    # Loop through players (Player 1 and CPU)
    for i in range(len(players)):
        # Set the current player and defending player
        current_player = i      # current_player is the one taking the current turn, and defending_player is the opponent.
        defending_player = 1 if i == 0 else 0

        print(f"It's {players[current_player].get('name')} (P{current_player + 1}) turn to attack.")

        # CPU attack (randomly choose an attack)
        if current_player == 1:
            chosen_attack = choice(players[current_player]['attacks'])

        # User attack (let the user choose an attack)
        else:
            for idx, attack in enumerate(players[current_player]['attacks']):       # If it’s the CPU’s turn, a random attack is chosen.
                print(f"{idx}. {attack['name']} \t {attack['power']}")      # Display available attacks
            user_choice = int(input("Choose an attack: "))      # If it’s the user’s turn, they are prompted to pick an attack from the list.
            chosen_attack = players[current_player]['attacks'][user_choice]

        att_power = chosen_attack['power']  # The chosen attack’s power is applied to the opponent.

        # Check if the defending player will die from the attack.
        if players[defending_player]["life"] - att_power <= 0:  # If the defending player’s life drops to 0 or below, the game announces the winner and ends.
            print(f"☠️ KILLER BLOW ☠️")
            sleep(1)
            print(f"{players[defending_player].get('name').upper()} IS DEAD ‼️ ")
            sleep(1)

            # Display winning message
            congrats_string = f"🎈🎉🎊 Congratulations player {current_player + 1}!! 🎊🎉🎈"
            print("\n")
            print("🎈🎉🎊✨" * (len(congrats_string) // 7))
            print(congrats_string)
            if round == 1:
                print(f"You won after just {round} round!")
            else:
                print(f"You won after {round} rounds!")

            # End the game
            is_gameover = True
            break

        # Reduce the defending player's life by the attack power
        # If the game isn’t over, the opponent's life is reduced by the attack's power, and the game continues after a brief pause.
        players[defending_player]["life"] -= att_power
        print("\n")
        sleep(0.8)


# Comments explaining the code:
# LIFE constant: This sets the initial life points for each Pokémon.
# API request: The program requests a list of Pokémon from the PokéAPI and prints them with their IDs.
# init_pokemon() function: This initializes a Pokémon by fetching its data from the API, formatting its height and weight, and assigning four random moves.
# print_life() function: Prints the current life of both players in each round.
# Gameplay loop: The main battle loop allows each player (user and CPU) to take turns attacking. The user selects an attack, while the CPU selects a random attack. The loop continues until one Pokémon's life reaches 0.
# Winning condition: If a player's attack reduces the opponent's life to 0 or below, the game declares a winner and ends.
# This code meets the requirements for the project by using data from the PokéAPI, simulating a battle, and allowing players to attack in turns.
#
