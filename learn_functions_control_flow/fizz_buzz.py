# Practice control flow - Fizz Buzz

'''
Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz',
multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'
- go up to 100
- be able to substitute "fizz" and "buzz" numbers
- use functions
'''

def fizz_buzz(fizz, buzz, num):
    if num % fizz == 0 and num % buzz == 0:
        return True
    else:
        return False

def fizzes(fizz, num):
    if num % fizz == 0:
        return True
    else:
        return False

def buzzes(buzz, num):
    if num % buzz == 0:
        return True
    else:
        return False

# take user input for "fizz" and "buzz" numbers
fizz = int(input("Pick a number for 'Fizz': "))
buzz = int(input("Pick a number for 'Buzz': "))

# check every number from 1 to 100
for i in range(1,100):
    # check if both
    if fizz_buzz(fizz, buzz, i) == True:
        print("FizzBuzz")
    # if not, check if fizz OR buzz
    elif fizzes(fizz, i) == True:
        print("Fizz")
    elif buzzes(buzz, i) == True:
        print("Buzz")
    # else print out the number as is
    else:
        print(i)
