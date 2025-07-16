# Mix data about a user into a list

name = input("What is your name? ")
age = int(input("What is your age? "))
dob = input("What is you DOB? (DD/MM/YYYY) ")

user_details_list = [name, age, dob]
print(f'Name: {user_details_list[0]}')
print(f'Age: {user_details_list[1]}')
print(f'DOB: {user_details_list[2]}')

print(type(user_details_list[1]))

height = float(input("What is your height in cm? "))
user_details_list.append(height)
print(f'Height: {user_details_list[-1]}')