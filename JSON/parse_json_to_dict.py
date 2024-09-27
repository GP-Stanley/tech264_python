import json

# Open and read the JSON file
with open('servers.json', 'r') as json_file:
    servers = json.load(json_file)

# Print the type of "servers"
print(f'Type of servers: {type(servers)}')

# Print the dictionary record with the key "server1"
print(f'server1: {servers["server1"]}')

# Print the dictionary record with the key "server2"
print(f'server2: {servers["server2"]}')

# Print all keys and values
for key, value in servers.items():
    print(f"Key and value: '{key}' = '{value}'")
    for sub_key, sub_value in value.items():
        print(f"  Record key and sub value: '{sub_key}' = '{sub_value}'")
