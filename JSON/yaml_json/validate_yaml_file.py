# Create version of validate_json_file.py but for checking a YAML file
#
# import yaml
# import json
#
# with open('example.yaml', 'r') as yaml_file:
#     yaml_data = yaml.safe_load(yaml_file)
#
# with open('example.json', 'w') as json_file:        # converts from yaml to json.
#     json.dump(yaml_data, json_file, indent=2)       # end up with json file.
#
# # Output: 'example.json' file has been created!


## THIS DOESN'T WORK -- WHY????
import os
import sys
import yaml

if len(sys.argv) > 1:
    # Check if the file exists
    if os.path.exists(sys.argv[1]):
        # Open the file for reading
        with open(sys.argv[1], "r") as file:
            yaml.safe_load(file)
            file.close()
            print("YAML file is valid!")
    else:
        # Alert the user that the specified file does not exist
        print(f"ERROR: File '{sys.argv[1]}' not found")
else:
    print("ERROR: No JSON file was specified to check")
    print(f"Usage: {sys.argv[0]} <JSON filename>")