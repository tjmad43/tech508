# Tuples with "Stranded on a Desert Island" game
'''
Tuples are a collection of values like a list, only immutable
Immutable - not able to be modified
int, float, bool, strings and chars are also immutable,
- but the variable holding them can be reassigned

#essentials = ("bread", "eggs", "milk")
#print(essentials)
#print(essentials.count("bread"))
the code above counts how many times "bread" is in the tuple
'''

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")

#the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3)

# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")

# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
# make another tuple, concatenate
essentials_tuple = essentials_tuple + (essential_item4, )
#
print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)

