# Practice lists - Waiter Helper

# Outcome (By doing this you should): Practice using lists and dictionaries
# Script should act like a waiter at a restaurant taking orders


# Greet the user
print("Hello, I am your waiter")
customer_order_list = []
bill = 0.0

# Print a list of starters
starters = {"a": 4.99, "b": 3.70, "c": 6.99}
print(f'Here are the starters you can choose from: {starters}')

# Take an input for the user for their starter, check it's valid
starter_taken = False
while not starter_taken:
    starter = input("What is your starter? ")
    if starter in starters:
        customer_order_list.append(starter)
        bill += starters[starter]
        starter_taken = True
    else:
        print("Sorry, that isn't available. Please pick from the list.")

# Print a list of mains
mains = {"a": 9.49, "b": 13.99, "c": 17.99}
print(f'Here are the mains you can choose from: {mains}')

# Take an input for the user for their main course
main_taken = False
while not main_taken:
    main = input("What is your main? ")
    if main in mains:
        customer_order_list.append(main)
        bill += mains[main]
        main_taken = True
    else:
        print("Sorry, that isn't available. Please pick from the list.")

# Print a list of desserts
desserts = {"a":7.50, "b": 4.99, "c": 3.50}
print(f'Here are the desserts you can choose from: {desserts}')

# Take an input for the user for their dessert
dessert_taken = False
while not dessert_taken:
    dessert = input("What is your dessert? ")
    if dessert in desserts:
        customer_order_list.append(dessert)
        bill += desserts[dessert]
        dessert_taken = True
    else:
        print("Sorry, that isn't available. Please pick from the list.")

# Print all of the user's choices
print(f'Here are your choices: {customer_order_list}')

print(f'Your bill comes to £{bill:.2f}')
