# Group Task: Make Functions

# 1. Function with no argument
# def print_something():
#     print("Something")
# can call this function from anywhere in the code, as long as it's after the function has been defined
#print_something()

# 2. Function with one argument
def print_something(something):
        print(something)

print_something("Hello world")


# 3. Greeting function
# putting "argument: datatype" gives a hint of what datatype to pass when calling the function
def greet(name: str):
    print("Hello, my name is " + name + ".")

greet("Bob")
greet("Susan")


# 4&5. Two arguments, with default values
# specifying argument=value gives a default for the function to use if one isn't passed when called
def addition(int1=2, int2=2):
    return int1 + int2

num1 = 3
num2 = 3
print(addition())


# 6. Any number of arguments
# * accepts variable number of arguments and packs them into tuple
def print_every_number(*args):
    print(type(args))
    for i in args:
        print(i)

print_every_number(1, 2, 3, 4, 5)


# 7. Hint argument data type
'''
greet(24601)
expects string, not int
change def greet(name) to def greet(name: str)
#greet(1234)
now gives message "Expected type 'str', got 'int' instead" when hovered over
'''


# 8. Bring it all together
# "-> datatype" after the arguments is a hint about the datatype of the return
def division(int1: int=2, int2: int=5) -> float:
    return int1 / int2

a = 4
b = 6
print(division())


# 9. Good function practices
'''
- function names should be lower case and words separated_by_underscores
- names should be descriptive
- functions should only do ONE thing
- too many arguments should be avoided
- type hints are important for others to understand what a function does
- docstrings: use ''' ''' after defining the function to add a description of 
    what it does - use function.__doc__ to read this within code
- functions should have a return value, if not specified will be 'none'
'''