import json

# Open and read the JSON file
with open('json_yaml/servers.json', 'r') as json_file:
    servers = json.load(json_file)

print({type(servers)})              # Output: {<class 'dict'>}
print(servers)