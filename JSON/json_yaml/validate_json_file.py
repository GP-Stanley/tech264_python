import json
import sys
import os
import yaml

sys.argv.append("A file")

if len(sys.argv) > 1:
    # Check if the file exists
    if os.path.exists(sys.argv[1]):
        # Open the file for reading
        with open(sys.argv[1], "r") as file:
            # Parse the JSON file - if it loads then the file contains valid
# JSON
            json.load(file)
            file.close()
            print("JSON file is valid!")
    else:
        # Alert the user that the specified file does not exist
        print(f"ERROR: File '{sys.argv[1]}' not found")
else:
    print("ERROR: No JSON file was specified to check")
    print(f"Usage: {sys.argv[0]} <JSON filename>")




# Steps:
# ls
# cd JSON
# cd json_yaml
# ls
# python .\validate_json_file.py                    (arguments start immediately after 'python is run'. So, 'validate' file will be argument 1.
# ^^ this will come up as Error: the script validate_json_file.py is expecting a JSON file as an argument, but none was provided. To fix this, you need to specify the JSON file you want to validate when running the script.
# Answer: python .\validate_json_file.py .\servers.json
# Output: JSON file is valid!