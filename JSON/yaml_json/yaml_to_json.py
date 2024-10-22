# create a script to convert a YAML file to a JSON file.  (using json library)
# YAML to JSON Conversion: We read a YAML file, convert its contents to a dictionary, and then write that dictionary to a JSON file using json.dump().

import yaml  # Import the PyYAML library to work with YAML files
import json  # Import the json library to work with JSON files


def yaml_to_json(yaml_file, json_file):
    """
    Function to convert a YAML file to a JSON file.

    Args:
        yaml_file: Path to the input YAML file.
        json_file: Path to the output JSON file.
    """

    # Open the YAML file in read mode
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)  # Load the contents of the YAML file as a Python dictionary.
        # The safe_load function is used for safely loading the YAML file and
        # converting it into a Python object (usually a dictionary).

    # Open (or create) the JSON file in write mode
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)  # Dump the Python dictionary (data) into the JSON file.
        # json.dump writes the dictionary to the JSON file.
        # indent=4 is used to make the JSON file human-readable by indenting
        # the content with 4 spaces per level.


# Example of how the function is used:

yaml_file_path = "example.yaml"  # Define the path to the input YAML file
json_file_path = "example.json"  # Define the path to the output JSON file

# Call the function to perform the conversion from YAML to JSON
yaml_to_json(yaml_file_path, json_file_path)

# Print a message indicating the conversion is complete
print(f"Converted {yaml_file_path} to {json_file_path}")  # Output: Converted example.yaml to example.json


"""SCRIPT FOR YAML.MD
Explanation:
Imports:
yaml: This is the PyYAML library, which allows the script to read and parse YAML files.
json: This is Python's built-in library to read, write, and manipulate JSON data.

Function Definition (yaml_to_json):
Purpose: This function takes two arguments:
yaml_file: the path to the YAML file that will be read.
json_file: the path where the resulting JSON file will be written.
yaml.safe_load: The function reads the contents of the YAML file using yaml.safe_load(), which converts the YAML file into a Python dictionary (data). This method ensures safe loading by avoiding the execution of arbitrary code.
json.dump: After the YAML data is loaded into a dictionary, it is written to the specified JSON file using json.dump(). The indent=4 argument is used to format the JSON file with 4 spaces of indentation, making it more readable.

Main Example:
The paths for the input YAML file (yaml_file_path) and output JSON file (json_file_path) are defined.
The yaml_to_json function is called with these paths to perform the conversion.
After the conversion, a message is printed indicating that the YAML file has been successfully converted to JSON.

Key Points:
yaml.safe_load(): Reads the YAML content into a Python dictionary safely, avoiding the risks of executing arbitrary code that could occur with yaml.load().
json.dump(): Converts the Python dictionary to JSON and writes it to a file, with an indentation of 4 spaces to make the file human-readable.

This script is straightforward for converting YAML to JSON and can be used in command-line scripts, automation tasks, or as part of a larger project.
"""