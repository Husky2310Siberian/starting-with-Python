# populate a set
from os import remove

bag = {"eggs" , "apples" , "bananas" , "eggs"} #double eggs
print("----------------")
print(type(bag))
print("Initial set: " , bag)
print("----------------")
# add a new item in set
bag.add("oranges")
print("After adding oranges" , bag)
print("----------------")
# remove item
remove_item = bag.remove("eggs")
print("After removing eggs" , bag)
print("----------------")
# remove item
remove_item2 = "lemons"
if remove_item2 not in bag:
    print(f"No such item: {remove_item2} , in bag")
else:
    bag.remove(remove_item2)
    print("After removing lemons" , bag)

print("----------------")
# iterate through the set
for item in bag:
    print(item)
