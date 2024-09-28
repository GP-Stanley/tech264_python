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