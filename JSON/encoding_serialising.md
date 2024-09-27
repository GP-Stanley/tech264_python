## Encoding
* Translating data from one format to another. 
* More broad than serialisation.
* Relates with security aspect, data security.
* Converts data into an encoded format which can't be understood to anyone, except the decoder. 
* Often used for data compression, encryption, or transmission. 


## Serialising
* Converting an object or data structure into a format that can be stored or transmitted and later reconstructed.
* Converting objects into streams of data.
* Mostly relates with objects, while transferring over network.
* Converts an object or data structure into a format that can be stored or transmitted and later reconstructed. 
* Preserves the data relationships and structure, making it suitable for saving program state or transmitting objects2.

## Dumbed down definitions
### Encoding
* Think of encoding as a way to `change data from one form to another`. 
* Imagine you have a message in English and you want to send it to a friend who only understands Morse code. You’d need to `encode` your English message into Morse code.
  * **Purpose**: Often used to make data smaller (compression), keep it secret (encryption), or prepare it for sending over the internet. 
  * **Security**: Encoded data can look like gibberish to anyone who doesn’t know how to decode it. 
  * **Example**: Turning a text message into a series of beeps and pauses (Morse code). 

### Serialising
* Serialising is like `packing up an object or data structure` so it can be easily `stored or sent somewhere else`. 
* Imagine you have a toy robot with many parts, and you need to send it to a friend. You’d take it apart, pack the pieces into a box, and send it. Your friend can then unpack the box and reassemble the robot.
  * **Purpose**: Helps in saving the state of an object or sending it over a network.
  * **Data Relationships**: Keeps the connections between different parts of the data intact.
  * **Example**: Converting a complex object in a program into a format like JSON or XML, which can be easily stored or sent and then reconstructed later.


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

print(type(servers_dict))                            # Assigning to a Variable: The result of the json.dumps() function is assigned to a variable named json_string. This variable now holds the JSON-formatted string.
print(servers_dict)                                  # Output: {'server1': {'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}, 'server2': {'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}}
# Convert dictionary to JSON-formatted string        # json.dumps() to convert a dictionary  into a JSON-formatted string.
json_string = json.dumps(servers_dict, indent=4)     # indent=4 : call specifies that the JSON string should be pretty-printed with an indentation of 4 spaces. This makes the JSON string easier to read.
print(json_string)                                   # prints the JSON-formatted string to the console, so you can see the output.
print(type(json_string))                             # Output: <class 'str'>
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

print("JSON data: ", res)           # Output: JSON data:  {"name": "John", "age": 30, "city": "New York"}
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

# Convert dictionary to JSON file                           # This part opens a file named servers.json in write mode ('w').
with open('json_yaml/servers.json', 'w') as json_file:  # Open or create a file in write mode. 
  json.dump(servers_dict, json_file, indent=4)  # write the dictionary to the file in JSON format. 
```
## Explanation
* `json.dump()`: Writes the Python dictionary to a JSON file. Take the object. Convert dictionary straight to JSON file. 
* `json.dumps()`: 's' for string. Convert to a string.
* `indent=4`: Formats the JSON output to be more readable.

```python
import json

# Open and read the JSON file
with open('json_yaml/servers.json',
          'r') as json_file:  # 'with open' function: used to open a file and ensure it is properly closed after its suite finishes, even if an exception is raised. This is done using the with statement, which simplifies file handling by automatically managing the file’s opening and closing.
  servers = json.load(json_file)  # 'r': read mode, 'w': write mode.

print({type(servers)})  # Output: {<class 'dict'>}
print(servers)  # Checking the dictionary works.

# Output:
# Type of servers: <class 'dict'>
# server1: {'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}
# server2: {'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}
```
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
import json  # imports the json module, which allows us to work with JSON data in Python.

# Open and read the JSON file
with open('json_yaml/servers.json',
          'r') as json_file:  # with open('servers.json', 'r') as json_file: This opens a file named servers.json in read mode ('r'). The with statement ensures the file is properly closed after its suite finishes.
  servers = json.load(
    json_file)  # servers = json.load(json_file): This reads the JSON data from the file and converts it into a Python dictionary, storing it in the variable servers.

# Print the type of "servers"
print(
  f'Type of servers: {type(servers)}')  # This prints the type of the servers variable, which should be <class 'dict'> because JSON data is converted into a Python dictionary.

# Print the dictionary record with the key "server1"
print(
  f'server1: {servers["server1"]}')  # These lines print the values associated with the keys "server1" and "server2" in the servers dictionary.
# Print the dictionary record with the key "server2"
print(f'server2: {servers["server2"]}')

# Print all keys and values
for key, value in servers.items():  # This loop iterates over each key-value pair in the servers dictionary.
  print(f"Key and value: '{key}' = '{value}'")  # This prints each key and its corresponding value.
  for sub_key, sub_value in value.items():  # This nested loop iterates over each key-value pair within the value (which is itself a dictionary).
    print(
      f"  Record key and sub value: '{sub_key}' = '{sub_value}'")  # This prints each sub-key and its corresponding sub-value within the nested dictionary.
```
### Notes:
* `json.load()`: Reads the JSON file and parses its contents into a Python dictionary. 
* `type()`: Prints the type of the `servers` variable to confirm it’s a dictionary. 
* `for loop`: Iterates through the dictionary to print each key and its corresponding value, as well as the sub-keys and sub-values.

