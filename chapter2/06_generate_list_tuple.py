# Accepts a sequence of comma-separated numbers, from the user and generates a list and a tuple of those numbers.

# List --> A list is a container which holds comma separated values (items or elements) between square brackets where items or elements need not all have the same type. We can define a list as an object that contains multiple data items (elements). The contents of a list can be changed (modifiable) during program execution. The size of a list can also change during execution, as elements are added or removed from it.

# Tuple --> A tuple is container which holds a series of comma separated values (items or elements) between parentheses such as an (x, y) co-ordinate. Tuples are like lists, except they are immutable (i.e. you cannot change its content once created) and can hold mix data types.

values = input("Please insert comma-seperated numbers: ")

list = values.split(",")

tuple = tuple(list)

print('List: ' , list)

print('Tuple : ' , tuple)