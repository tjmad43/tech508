# Summary - Write a Python script to calculate the user's year of birth

age_int = 0
name_str = ""

name_str = input("What is your name? ")
age_int = int(input("What is your age? "))

birth_year = 2025 - age_int

print(f'OMG, you are {age_int} years old so you were born in {birth_year}.')
