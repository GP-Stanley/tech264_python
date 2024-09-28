# Create version of validate_json_file.py but for checking a YAML file

import yaml
import json

with open('example.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

with open('example.json', 'w') as json_file:
    json.dump(yaml_data, json_file, indent=2)

# Output: 'example.json' file has been created!