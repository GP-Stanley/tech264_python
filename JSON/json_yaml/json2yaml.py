# create a script that converts Valid JSON to Valid YAML.
#
#
# Valid JSON:
#
# {
#   "name": "John Doe",
#   "age": 30,
#   "isStudent": False,
#   "courses": ["Python", "DevOps"],
#   "address": {
#     "street": "123 Main St",
#     "city": "Anytown"
#   }
# }
#
# """
# Valid YAML:
#
# name: John Doe
# age: 30
# isStudent: false
# courses:
#   - Python
#   - DevOps
# address:
#   street: 123 Main St
#   city: Anytown
# """

# Starting code:

import json
import os
import sys
import yaml

sys.argv.append("yaml_servers")

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

#------------------------------------------------------------------------
# OUR FIRST TRY
with open(sys.argv[1], "r") as json_file:
    json_data = json.load(json_file)

    if len(sys.argv) > 2 and not os.path.exists(sys.argv[2]):
        target_file = sys.argv[2]
        print(f"Target file: {target_file}")

        with open(f"{target_file}.yaml", "w") as yaml_file:
                yaml.dump(json_data, yaml_file)
    else:
        yaml_obj = yaml.dump(json_data)
        print(yaml_obj)

#-----------------------------------------------------------------------
# ANOTHER GROUPS EXAMPLE:
#
# 1. Convert the JSON to YAML - use yaml library
# # Open the JSON file and read its contents
# yaml_data = yaml.dump(source_content)                   # The yaml.dump method converts the JSON content to YAML format.
# print(yaml_data)
#
# # 2. Save the YAML into a new file with the name for it received as a argument
# # 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
# if not len(sys.argv) > 2:
#     print(yaml_data)
#     sys.exit(1)
#
# # 2.2 Check the target file doesn't already exist
# if os.path.exists(sys.argv[2]):
#         print(f"Error: The file '{sys.argv[2]}' already exists. Please choose a different file name.")
#
# # 2.3 If previous conditions not met, then save YAML file
# else:
#     with open(sys.argv[2], 'w') as yaml_file:
#         yaml_file.write(yaml_data)


# You need to find a way to convert the JSON object to a YAML object and
# then save that YAML in a new target YAML file (name of YAML file is specified as an argument by the user)
#
# We will talk through it on xxx so be ready to present your solution!
#
# Hints:
# * The method you need may involve “dumping”
# * Before you can import yaml, you may need to install the pyyaml module with this command: pip install pyyaml
# * Get the groups to let you know if they complete the task. At the 60 minute mark bring everyone back and talk through the completed code.
#
# Post a link to this task in the chat at COB
#