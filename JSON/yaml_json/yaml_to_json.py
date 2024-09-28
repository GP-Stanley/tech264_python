# create a script to convert a YAML file to a JSON file.  (using json library)

import yaml
import json

def yaml_to_json(yaml_file, json_file):         # This function converts a YAML file to a JSON file. yaml_file: Path to the YAML file : json_file: Path to the output JSON file.
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)             # Load the yaml file.

    with open(json_file, "w") as file:          # Write the data to a json file.
        json.dump(data, file, indent=4)

# Example
yaml_file_path = "example.yaml"
json_file_path = "example.json"
yaml_to_json(yaml_file_path, json_file_path)
print(f"Converted {yaml_file_path} to {json_file_path}")
