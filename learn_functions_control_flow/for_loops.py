# Working with 'for loops'

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# 1. Loop through a list, printing doubles
for num in list_data:
    print(num * 2)

# 2. Loop through the 'embedded_lists' list &
# 3. Loop through the lists embedded inside a list
for data in embedded_lists:
    print(data)
    for item in data:
        print(item)

# 4. Loop through a dictionary
for key in dict_data:
    print(key)

# 5. Loop through a dictionary and print its values &
# 6. Loop to print the values of the dictionary items inside a dictionary
for value in dict_data:
#    print(dict_data[value])
    for i in dict_data[value]:
        print(dict_data[value][i])

# 7. Loop to print specific values of the dictionary items inside a dictionary
for value in dict_data:
    print(dict_data[value]["money"])

# 8. Loop through a list with a nested if statement
for x in list_data:
    if x < 3:
        print("less than 3")
    elif x == 3:
        print("I found three")
    elif x > 3:
        print("greater than 3")