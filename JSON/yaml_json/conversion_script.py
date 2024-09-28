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