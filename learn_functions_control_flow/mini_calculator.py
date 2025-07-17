# Practice functions - Mini calculator

def add(int1, int2):
    return int1 + int2

def subtract(int1, int2):
    return int1 - int2

def multiply(int1, int2):
    return int1 * int2

def divide(int1, int2):
    return int1 / int2

end = False
while not end:
    options = ["add", "subtract", "multiply", "divide", "exit"]
    valid = False
    while not valid:
        print(f'What would you like to do? Here are the options: {options}')
        option = input("> ")
        if option in options:
            valid = True
        else:
            print("Sorry, please pick from the avilable options.")


    if option == "exit":
        end = True
    else:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if option == "add":
            print(add(num1, num2))
        elif option == "subtract":
            print(subtract(num1, num2))
        elif option == "multiply":
            print(multiply(num1, num2))
        elif option == "divide":
            print(divide(num1, num2))



