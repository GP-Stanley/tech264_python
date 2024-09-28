# Validating a yaml file.

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