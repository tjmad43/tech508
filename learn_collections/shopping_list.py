# Working

shopping_list = ["eggs","bread","bananas","biscuits","milk"]

print(shopping_list)
print(type(shopping_list))
# first item
print(shopping_list[0])
# last item
print(shopping_list[-1])

# change second item
shopping_list[1] = "rice"
print(shopping_list[1])

# adding items
shopping_list.append("carrots")
print(len(shopping_list))
shopping_list = shopping_list + ["toffee","coffee"]
print(shopping_list)

# removing items
shopping_list.remove("bananas")
print(shopping_list)

shopping_list.pop(-1)
print(shopping_list)