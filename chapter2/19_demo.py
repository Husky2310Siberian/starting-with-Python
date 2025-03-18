# Falsy - Truthy Values
# 0 , 0.0 , 0j , "" , [] , {} , set() , False , None

empty_dict = {}
print(type(empty_dict))

a = 5

if a > 0 and a < 10:
    print("Valid number")

# more efficient
if 0 < a < 10:
    print("Valid number")

students = ("Alice" , "Bob" , "Charlie")

students = tuple(["Siberian"] + list(students)[1:])
print(students)