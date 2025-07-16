# Working with sets

# Sets store multiple items in a single variable.
# They are unordered, unindexed and items are unchangeable (but can be added and removed)
# Unlike lists and dictionaries, duplicates are not allowed

fruits = {"apple", "banana", "cherry"}
print(fruits)

# add item
fruits.add("orange")
print(fruits)

# remove item
fruits.remove("banana")
print(fruits)

# duplicates cannot be added
fruits.add("apple")
print(fruits)
# there is still only one apple in the set

# print 2nd item?
#print(fruits[1])
# does not work since the items have no order or index