# Summary - Write a Python script to calculate the user's year of birth
import datetime

name_str = input("What is your name? ")
age_int = int(input("What is your age? "))
month = int(input("What month were you born? (number e.g. 07) "))
day = int(input("What day were you born? "))

# figure out birth year /then/ calculate hours
today = datetime.datetime.today()
current_month = today.month
current_day = today.day

# if they've had a birthday already this year, then subtract age from current year
# if not, subtract an extra year
if current_month == month:
    if current_day <= day:
        birth_year = today.year - age_int -1
    else:
        birth_year = today.year - age_int
elif current_month >= month:
    birth_year = today.year - age_int
else:
    birth_year = today.year - age_int - 1

print(f'OMG {name_str}, you are {age_int} years old so you were born in {birth_year}.')

# Calculate hours passed by subtracting birthday from today's date
# convert days (given by the datetime function) to hours
bday = datetime.datetime(birth_year, month, day)
days_delta = today - bday
hours = days_delta.days * 24

print(f'You have lived {hours} hours!')



# # test of hours
# my_days = (365.25*25) + 197
# my_hours = my_days * 24
# print(my_hours)