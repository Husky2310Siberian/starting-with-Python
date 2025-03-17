items = [1 , 2 , 3.14 , True , "Hello World"]

for item in items:
    print(item , end=" ")
print()

nested_list = [[1 , 2] , [3 , 4] , [5 , 6]]

print(f"nested list {nested_list}")

print(f"First nested list {nested_list[0]}")

print(f"First element of second nested list is {nested_list[1][0]}")
print(f"Second element of third nested list is {nested_list[2][1]}")

for outer_item in nested_list:  # outer_item --> [1,2] etc
    for inner_item in outer_item: # inner_item --> 1 , 2 , 3 etc.
        if inner_item % 2 == 0:
            result = inner_item

print("Final even is: " , result)
