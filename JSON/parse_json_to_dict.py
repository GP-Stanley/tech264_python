import json                                                     # imports the json module, which allows us to work with JSON data in Python.

# Open and read the JSON file
with open('json_yaml/servers.json', 'r') as json_file:          # with open('servers.json', 'r') as json_file: This opens a file named servers.json in read mode ('r'). The with statement ensures the file is properly closed after its suite finishes.
    servers = json.load(json_file)                              # servers = json.load(json_file): This reads the JSON data from the file and converts it into a Python dictionary, storing it in the variable servers.

# Print the type of "servers"
print(f'Type of servers: {type(servers)}')                      # This prints the type of the servers variable, which should be <class 'dict'> because JSON data is converted into a Python dictionary.

# Print the dictionary record with the key "server1"
print(f'server1: {servers["server1"]}')                         # These lines print the values associated with the keys "server1" and "server2" in the servers dictionary.
# Print the dictionary record with the key "server2"
print(f'server2: {servers["server2"]}')

# Print all keys and values
for key, value in servers.items():                              # This loop iterates over each key-value pair in the servers dictionary.
    print(f"Key and value: '{key}' = '{value}'")                # This prints each key and its corresponding value.
    for sub_key, sub_value in value.items():                    # This nested loop iterates over each key-value pair within the value (which is itself a dictionary).
        print(f"  Record key and sub value: '{sub_key}' = '{sub_value}'")           # This prints each sub-key and its corresponding sub-value within the nested dictionary.
