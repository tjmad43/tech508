#Examples of variables

num = 10
decimal = 10.1
string = "hello"
# using == compares values rather than assigning one

print(num, type(num))
print(decimal, type(decimal))
print(string, type(string))

# python is strongly typed, meaning variables of different types have to be converted
# to the same one in order to perform an operation on the two together
# for example:
print(str(num) + string)
# in this case a weakly typed language would implicitly convert num into a string

# python is a dynamically typed language, meaning that types are determined at
# runtime and don't have to be declared, as demonstrated with the tyype() function above

print(id(num))
num = 7
print(id(num))
# the id changes because the variable has been reassigned to a new object


x = 10
y = x
print(id(x))
print(id(y))
# the id of x and y are the same because they point to the same object
# the id of both would change (to the same thing) if x were reassigned

name = input("What is your name? ")
age =  input("Age: ")
dob = input("Date of birth: ")
print(name + ", " + age + ", " + dob)