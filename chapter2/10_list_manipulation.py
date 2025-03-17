# Populate
fruits = ["Apple", "Banana", "Cherry" , "Apple"]

print("Initial list of fruits: " , fruits)

# Add
fruits.append("Berry")
print("New list of fruits, after adding Berry:" , fruits)

# Add two or more items in list
# fruits.append(["Grapes" , "Fig"])   # the two items are in a new nested list
# print("New list of fruits: " , fruits)

# Add two or more items in list
fruits.extend(["Grapes", "Fig"])
print("New list of fruits, after adding Grapes and Fig:" , fruits)

# Insert one item in a specific position
fruits.insert(1 , "Coconut")
print("New list of fruits, after adding Coconut:" , fruits)

# Update an item
fruits [0] = "Melon"
print("New list of fruits, after updating Melon:" , fruits)

# Update two items
# print(fruits[1:3])
fruits[1:3] = ["COCONUT" , "BANANA"]
print("New list of fruits, after updating two elements:" , fruits)

# Delete

removed_item2 = fruits.remove("Apple")
print(f"removed_item2 : {removed_item2}")
print("New list of fruits, after removing Apple:" , fruits)

# Delete with pop
removed_item = fruits.pop(1)
print(f"Removed fruit '{removed_item}' from fruits:")
print("New list of fruits, after removing COCONUT:" , fruits)

if removed_item in fruits:
    print(f"Removed fruit '{removed_item}' from fruits:")
else:
    print(f"'{removed_item}' does not exist in fruits:")

# search

position = fruits.index("Cherry")
print(f"{position}th fruit in fruits:" , fruits[position])