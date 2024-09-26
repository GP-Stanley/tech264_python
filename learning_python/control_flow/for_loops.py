list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for num in list_data:
    print(num * 2)

    [1, 2, 3]
    [4, 5, 6]

    for data in embedded_lists:
        print(data)


for data in embedded_lists:
    print(data)
    for item in data:
        print(item)


for key in dict_data:
    print(key)


for value in dict_data.values():
    print(value)
# Output:
# {'name': 'Bronson', 'money': '$0.05'}
# {'name': 'Masha', 'money': '$3.66'}
# {'name': 'Roscoe', 'money': '$1.14'}


for value in dict_data.values():
    for inner_value in value.values():
        print(inner_value)


for value in dict_data.values():
    print(value)
    for inner_value in value.values():
        print(inner_value)


for value in dict_data.values():
    print(value["money"])

    list_data = [1, 2, 3, 4, 5]

    for number in list_data:
        if number < 3:
            print('less than 3')
        elif number == 3:
            print('I found three')
        else:
            print('greater than 3')