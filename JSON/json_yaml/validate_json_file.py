import os
import sys
import json

if len(sys.argv) > 1:
    # Check if the file exists
    if os.path.exists(sys.argv[1]):
        # Open the file for reading
        with open(sys.argv[1], "r") as file:
            # Parse the JSON file - if it loads then the file contains valid JSON
            json.load(file)
            print("JSON file is valid!")
    else:
        # Alert the user that the specified file does not exist
        print(f"ERROR: File '{sys.argv[1]}' not found")
else:
    print("ERROR: No JSON file was specified to check")
    print(f"Usage: {sys.argv[0]} <JSON filename>")

# ERROR: No JSON file was specified to check
# Usage: C:\Users\georg\OneDrive - Sparta Global\Documents\GitHub Repos\tech264_python\JSON\validate_json_file.py <JSON filename>



# Steps:
# ls
# cd JSON
# cd json_yaml
#
#