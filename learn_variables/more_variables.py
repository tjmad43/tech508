#Task: Concatenate these variables with different data types
# concatenation is joining two strings (or other values) to form a single value
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print(str(x) + str(y) + z)

'''
'''

#Task: Convert/cast this string to an int and float
int_string = "6"

# convert int_string to an integer
int_string = int(int_string)

# after converting, print its data type to the screen
print(type(int_string))

# convert int_string to float
int_string = float(int_string)

# after converting, print its data type to the screen
print(type(int_string))


'''
'''

#Task: Print line as an f-string
name = "Lassie"
years = 7
height_cm = 60.2

# print these variables in an f-string so that it outputs this to the screen:
# "Lassie is 7 years old and 60.2 cm tall."
print(f'{name} is {years} years old and {height_cm} cm tall.')


'''
'''

#Task: Use f-strings to format numbers
pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f'Pi to 3 decimal places: {pi:.3f}')
# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f'Pi to 5 decimal places: {pi:.5f}')


score = 16
max_score = 26
score_as_decimal = score/max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f'You scored {score_as_decimal}')
# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f'You scored {score_as_decimal * 100:5f}%')
# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f'You scored {score_as_decimal * 100:.2f}%')
# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'
print(f'You scored {score_as_decimal * 100:.0f}%')