# Group Task: Make Functions

# 1&2. Function with no argument, one argument

def print_something(something):
        print(something)

print_something("Hello world")


# 3. Greeting function

def greet(name: str):
    print("Hello, my name is " + name + ".")

greet("Bob")
greet("Susan")


# 4&5. Two arguments, default values

def addition(int1=2, int2=2):
    return int1 + int2

num1 = 3
num2 = 3
print(addition(num1, num2))


# 6. Any number of arguments

# * accepts variable number of arguments and packs them into tuple
def print_every_number(*args):
    print(type(args))
    for i in args:
        print(i)

print_every_number(1, 2, 3, 4, 5)


# 7. Hint argument data type
'''
#greet(24601)
expects string, not int
change def greet(name) to def greet(name: str)
#greet(1234)
now gives message "Expected type 'str', got 'int' instead" when hovered over
'''


# 8. Bring it all together

def division(int1: int=2, int2: int=5) -> float:
    return int1 / int2

a = 4
b = 6
print(division(a,b))


# 9. Good function practices
'''
- function names should be lower case and words separated_by_underscores
- names should be descriptive
- functions should only do ONE thing
- over 3 arguments should be avoided
'''