import json

person = {
    'name' : 'Carol',
    'age' : 43,
    'weight' : 160,
    'dogs' : ['Mr. Barks', 'Rufus']
}

with open(',/person.json', 'w') as output:
    json.dump(person, output)