## JSON and YAML file
```python
# Valid JSON:
{
  "name": "John Doe",
  "age": 30,
  "isStudent": False,
  "courses": ["Python", "DevOps"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}

# Valid YAML:

name: John Doe
age: 30
isStudent: false
courses:
  - Python
  - DevOps
address:
  street: 123 Main St
  city: Anytown
```

## Task 1
* Create version of parse_json_to_dict.py but for parsing/converting YAML to a dictionary
```python
def parse_yaml_to_dict(yaml_file):              # This function reads a yaml file and converts it to a Python dictionary. yaml_file: Path to the yaml file.
    with open(yaml_file, "r") as file:          # with open statement loads a file in python: Load the yaml file.
        data = yaml.safe_load(file)
    return data                                 # Dictionary representation of the yaml file.

# Example
yaml_file_path = 'example.yaml'
yaml_dict = parse_yaml_to_dict(yaml_file_path)
print(yaml_dict)
```
## Task 1: working version
```python
# Create a script to parse a YAML file and convert it to a Python dictionary.
# Parsing yaml to Dictionary: We read a yaml file and convert its contents into a Python dictionary using yaml.safe_load().

import yaml
from pprint import pprint


with open('example.yaml', "r") as yaml_file:          # with open statement loads a file in python: Load the yaml file.
    output = yaml.safe_load(yaml_file)                # 'safe.load()' : is safe for untrusted input.

# pprint (output)
pprint(output)                                        # print the whole dictionary.
print(output['server1']['status'])                    # This is where we can request a particular part of the key. E.g., 'server1' : 'status' = (output) active.



"""Output:
{'server1': {'hostname': 'web-server-1',
             'ip_address': '192.168.1.1',
             'role': 'web',
             'status': 'active'},
 'server2': {'hostname': 'db-server-1',
             'ip_address': '192.168.1.2',
             'role': 'database',
             'status': 'maintenance'}}
active
"""
```

## Task 2
* Create version of validate_json_file.py but for checking a YAML file
```python
import yaml

def validate_yaml_file(yaml_file):              #  This function checks if a yaml file is valid. yaml_file: Path to the YAML file
    try:
        with open(yaml_file, "r") as file:
            yaml.safe_load(file)
        return True                             # return: True if valid, False otherwise.
    except yaml.YAMLError as e:
        print(f"Error in YAML file: {e}")
        return False

# Example
yaml_file_path = 'example.yaml'
is_valid = validate_yaml_file(yaml_file_path)
print(f"Is the YAML file valis? {is_valid}")
```
## Task 2: working version
```python
# Create version of validate_json_file.py but for checking a YAML file

import yaml
import json

with open('example.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

with open('example.json', 'w') as json_file:
    json.dump(yaml_data, json_file, indent=2)

# Output: 'example.json' file has been created!
```

## Task 3
* Create a YAML to JSON file conversion script
```python
import yaml
import json

def convert_yaml_to_json(yaml_file, json_file):
    with open(yaml_file, "r") as yf:
        yaml_data = yaml.safe_load(yf)
    with open(json_file, "w") as jf:
        json.dump(yaml_data, jf, indent=4)

# Example
convert_yaml_to_json('example.yaml', 'servers.json')

# Output: 'example.json' is made and 'servers.json' is made!
```

## Task 4
* Create a script that check if an entire folders contents is valid YAML (will need loops to check each file)
```python
# create a script to check if all files in a folder are valid YAML files. This will involve looping through each file in the folder.
# Validating YAML Files in a Folder: We loop through all files in a folder, check if they are YAML files, and validate each one.

import yaml
import os

def validate_yaml_folder(folder_path):          # This function checks if all yaml files in a folder are valid.
    validation_results = {}

    for filename in os.listdir(folder_path):                            # folder_path: Path to the folder.
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            file_path = os.path.join(folder_path, filename)
            is_valid = validate_yaml_file(file_path)
            validation_results[filename] = is_valid

    return validation_results                                           # Dictionary with file names as keys and validation status as values.


# Example usage
folder_path = 'example_folder'
results = validate_yaml_folder(folder_path)
for file, is_valid in results.items():
    print(f"{file}: {'Valid' if is_valid else 'Invalid'}")``'
```
## Task 4
* Create a script that check if an entire folders contents is valid YAML (will need loops to check each file)
```python
# Create a script that check if an entire folders contents is valid YAML (will need loops to check each file)

import os
import yaml

def is_valid_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        return True
    except yaml.YAMLError:
        return False

def check_folder_for_yaml(folder_path):
    for root, dirs, files in os.walk(folder_path):                          # uses os.walk() to iterate through all files in the given folder and its subfolders.
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.yaml') or file_path.endswith('.yml'):   # For each file, it checks if the file extension is .yaml or .yml.
                if not is_valid_yaml(file_path):                            # It then calls is_valid_yaml to check if the file is valid YAML and prints the result.
                    print(f"Invalid YAML: {file_path}")
                else:
                    print(f"Valid YAML: {file_path}")

# the path to your folder.                      # script sets the folder path to 'yaml_json' and calls check_folder_for_yaml with this path.
folder_path = "C:\\Users\\georg\\OneDrive - Sparta Global\\Documents\\GitHub Repos\\tech264_python\\json\\yaml_json"
check_folder_for_yaml(folder_path)


# Output: Valid YAML: C:\Users\georg\OneDrive - Sparta Global\Documents\GitHub Repos\tech264_python\json\yaml_json\example.yaml
```