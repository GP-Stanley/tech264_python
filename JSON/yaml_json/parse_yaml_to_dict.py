#  create a script to parse a YAML file and convert it to a Python dictionary.

import yaml

def parse_yaml_to_dict(yaml_file):              # This function reads a yaml file and converts it to a Python dictionary. yaml_file: Path to the yaml file.
    with open(yaml_file, "r") as file:          # Load the yaml file.
        data = yaml.safe_load(file)
    return data                                 # Dictionary representation of the yaml file.

# Example
yaml_file_path = 'example.yaml'
yaml_dict = parse_yaml_to_dict(yaml_file_path)
print(yaml_dict)



"""Appeared in Terminal Window
Type of servers: <class 'dict'>
server1: {'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}
server2: {'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}
Key and value: 'server1' = '{'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}'
  Record key and sub value: 'hostname' = 'web-server-1'
  Record key and sub value: 'ip_address' = '192.168.1.1'
  Record key and sub value: 'role' = 'web'
  Record key and sub value: 'status' = 'active'
Key and value: 'server2' = '{'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}'
  Record key and sub value: 'hostname' = 'db-server-1'
  Record key and sub value: 'ip_address' = '192.168.1.2'
  Record key and sub value: 'role' = 'database'
  Record key and sub value: 'status' = 'maintenance'
"""