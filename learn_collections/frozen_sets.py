# Working with frozen sets

frozen_set = frozenset({"hello", "world"})

# add item to frozen set?
#frozen_set.add("!")
# AttributeError: 'frozenset' object has no attribute 'add'
# cannot add items to a frozen set, it is (unlike a normal set) completely unchangeable

normal_set = {"let's", "learn"}

normal_set.add(frozen_set)
# works because frozen_set isn't itself being changed

print(normal_set)
# order that frozen_set appears is random because normal_set is unordered

