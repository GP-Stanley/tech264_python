import json     # import json imports Python's built-in json module, which provides functions to work with JSON data (converting between JSON and Python objects).

person = {      # A dictionary named person is created, representing information about an individual. This dictionary has four keys
    'name' : 'Carol',
    'age' : 43,
    'weight' : 160,
    'dogs' : ['Mr. Barks', 'Rufus']
}

with open('/person.json', 'w') as output:      # opens a file named person.json in write mode ('w'). The with statement ensures the file is automatically closed after the block of code completes.
    json.dump(person, output)           #  converts the person dictionary into a JSON format and writes it to the person.json file.


# SUMMARY:
# This code creates a dictionary (person), then converts it into a JSON-formatted string,
# and writes it to a file (person.json). The file will contain a JSON representation of the person dictionary.