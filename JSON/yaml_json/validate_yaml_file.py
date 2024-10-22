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


import os   # Import os to check for file existence
import sys  # Import sys to handle command-line arguments
import yaml # Import PyYAML to work with YAML files

# Check if the user provided a file name as a command-line argument
if len(sys.argv) > 1:
    # Check if the specified YAML file exists
    if os.path.exists(sys.argv[1]):
        # Open the file in read mode
        with open(sys.argv[1], "r") as file:
            yaml.safe_load(file)  # This validates the YAML format by trying to load it
            file.close()  # Close the file (although unnecessary here since 'with' closes it automatically)
            print("YAML file is valid!")  # Print a success message if the file is valid
    else:
        # Error message if the file does not exist
        print(f"ERROR: File '{sys.argv[1]}' not found")
else:
    # Error message if no file was provided as a command-line argument
    print("ERROR: No YAML file was specified to check")
    print(f"Usage: {sys.argv[0]} <YAML filename>")


"""NOTES FOR YAML.MD LATER:
Detailed Explanation of the Code:
Imports:

os: Used to check if the specified YAML file exists on the system.
sys: Handles command-line arguments to allow users to specify the file to check.
yaml: Used for loading and validating the YAML content.
Command-Line Argument Check:

The script checks if the user has provided a file path as a command-line argument (len(sys.argv) > 1).
If no argument is provided, the script prints an error message and gives usage instructions.
File Existence Check:

If the argument is provided, the script checks whether the file exists at the given path using os.path.exists(sys.argv[1]).
If the file doesn't exist, an error message is displayed.
YAML Validation:

If the file exists, the script opens it in read mode ("r") and attempts to parse it using yaml.safe_load().
If the file contains valid YAML, yaml.safe_load() loads it as a Python dictionary or list. If the YAML is invalid, an exception will be raised.
File Closure:

file.close() is called manually, but this is unnecessary when using the with statement because with automatically closes the file after the block of code completes.
Output:

If the YAML file is valid, it prints "YAML file is valid!".
If the YAML file is invalid, yaml.safe_load() will raise an exception, but this is not handled in the current code, so the script will exit with an error message.
Why Doesn't It Work? (Problems)
Error in the Error Message:

The line print("ERROR: No JSON file was specified to check") mistakenly refers to a JSON file instead of a YAML file. It should say:
(python)


Copy code
print("ERROR: No YAML file was specified to check")
Lack of Exception Handling:

The script does not handle the exception that yaml.safe_load() raises if the YAML file is invalid. If you want to validate the YAML and gracefully handle errors, you need to add exception handling. Here's how you can do that:
"""

"""FIXED CODE WITH EXCEPTION HANDLING:
import os
import sys
import yaml

# Check if the user provided a file name as a command-line argument
if len(sys.argv) > 1:  
    # Check if the specified YAML file exists
    if os.path.exists(sys.argv[1]):  
        try:
            # Open the file in read mode
            with open(sys.argv[1], "r") as file:
                yaml.safe_load(file)  # Attempt to load the YAML content
                print("YAML file is valid!")  # Success message if no exception occurs
        except yaml.YAMLError as e:  # Catch YAML parsing errors
            print(f"Invalid YAML file: {e}")  # Print error message with details
    else:
        # Error message if the file does not exist
        print(f"ERROR: File '{sys.argv[1]}' not found")
else:
    # Error message if no file was provided as a command-line argument
    print("ERROR: No YAML file was specified to check")
    print(f"Usage: {sys.argv[0]} <YAML filename>")

"""

"""EXPLANATION OF FIXES:
Explanation of Fixes:
Exception Handling:

Added try-except block around yaml.safe_load() to catch and display yaml.YAMLError if the YAML content is invalid.
Corrected Error Message:

Fixed the incorrect error message from "No JSON file was specified" to "No YAML file was specified."
Example Usage:
(bash)
Copy code
python validate_yaml_file.py example.yaml
If valid: It will print YAML file is valid!
If invalid: It will catch and print the YAML parsing error
"""