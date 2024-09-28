# Create a script to parse a YAML file and convert it to a Python dictionary.
# Parsing yaml to Dictionary: We read a yaml file and convert its contents into a Python dictionary using yaml.safe_load().

import yaml
from pprint import pprint


with open('example.yaml', "r") as yaml_file:          # with open statement loads a file in python: Load the yaml file.
    output = yaml.safe_load(yaml_file)                # 'safe.load()' : is safe for untrusted input.

# pprint (output)
pprint(output)                                        # print the whole dictionary.
print(output['server1']['status'])                    # This is where we can request a particular part of the key. E.g., 'server1' : 'status' = (output) active.



"""Output:
{'server1': {'hostname': 'web-server-1',
             'ip_address': '192.168.1.1',
             'role': 'web',
             'status': 'active'},
 'server2': {'hostname': 'db-server-1',
             'ip_address': '192.168.1.2',
             'role': 'database',
             'status': 'maintenance'}}
active
"""