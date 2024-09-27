## Encoding
* Translating data from one format to another. 
* More broad than serialisation.
* Converting one stream of data to another stream of data.
* Relates with security aspect, data security.
* Converts data into an encoded format which can't be understood to anyone, except the decoder. 
* Often used for data compression, encryption, or transmission. 


## Serialising
* About moving structured data over a storage/transmission medium in a way that the structure can be maintained. 
* Converting an object or data structure into a format that can be stored or transmitted and later reconstructed.
* Converting objects into streams of data.
* Mostly relates with objects, while transferring over network.
* Converts an object or data structure into a format that can be stored or transmitted and later reconstructed. 
* Preserves the data relationships and structure, making it suitable for saving program state or transmitting objects2.

### Subtasks
1. Convert this Python dictionary into a JSON-formatted string.

```python
import json
# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# Convert dictionary to JSON-formatted string
json_string = json.dumps(servers_dict, indent=4)
print(json_string)
```
## Notes:
* `json.dumps()`: Converts the Python dictionary to a JSON-formatted string. 

## My example
* we're converting this dictionary into Json data.
* `.dumps()`: dump string. Whatever you put in here, you want to convert to json. We want to convert some 'data'.
* `res`: creating your response. 
```python
import json                         # import json.

def convert_json(data):             # function is called 'convert_json': parameters is 'data'.
    json_string = json.dumps(data)  # creating a json string. it's value is 'json.dumps()'
    return json_string

my_data = {'name': 'John',          # dict (my_data).
           'age': 30,
           'city': 'New York'}

res = convert_json(my_data)         # response. Calling in function.

print("JSON data: ", res)

# Output: JSON data:  {"name": "John", "age": 30, "city": "New York"}
```

2. Convert this Python dictionary to a JSON file.

```python
import json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# Convert dictionary to JSON file
with open('servers.json', 'w') as json_file:
    json.dump(servers_dict, json_file, indent=4)
```
## Explanation
* `json.dump()`: Writes the Python dictionary to a JSON file. 
* `indent=4`: Formats the JSON output to be more readable.

By performing these tasks, you are serialising the Python dictionary into JSON format, which can be stored or transmitted and later reconstructed.


## Convert JSON file to Python dictionary
### Steps:
Create a new file servers.json and add this JSON to it:

```python
{
	"server1": {
		"hostname": "web-server-1",
		"ip_address": "192.168.1.1",
		"role": "web",
		"status": "active"
	},
	"server2": {
		"hostname": "db-server-1",
		"ip_address": "192.168.1.2",
		"role": "database",
		"status": "maintenance"
	}
}
```
* Create a file called parse_json_to_dict.py and add code to it to: Steps:
  * Use 'with' to open the file created above 
  * Parse contents the JSON file into a Python dictionary named "servers"
  * Print out the type of "servers"
  * Print out the dictionary record with the key "server1"
  * Print out the dictionary record with the key "server2"
  * Print all of the keys and values. Output should be:

```python
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

# Output:
# Type of servers: <class 'dict'>
# server1: {'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}
# server2: {'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}
# Key and value: 'server1' = '{'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}'
#   Record key and sub value: 'hostname' = 'web-server-1'
#   Record key and sub value: 'ip_address' = '192.168.1.1'
#   Record key and sub value: 'role' = 'web'
#   Record key and sub value: 'status' = 'active'
# Key and value: 'server2' = '{'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}'
#   Record key and sub value: 'hostname' = 'db-server-1'
#   Record key and sub value: 'ip_address' = '192.168.1.2'
#   Record key and sub value: 'role' = 'database'
#   Record key and sub value: 'status' = 'maintenance'
```
### Notes:
* `json.load()`: Reads the JSON file and parses its contents into a Python dictionary. 
* `type()`: Prints the type of the `servers` variable to confirm it’s a dictionary. 
* `for loop`: Iterates through the dictionary to print each key and its corresponding value, as well as the sub-keys and sub-values.




