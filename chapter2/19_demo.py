# Falsy - Truthy Values
# 0 , 0.0 , 0j , "" , [] , {} , set() , False , None
from numpy.f2py.crackfortran import endpattern

empty_dict = {}
print(type(empty_dict))

empty_set = set()
print(type(empty_set))

a = 5
if a > 0 and a < 10:
    print("Valid number")

# more efficient
if 0 < a < 10:
    print("Valid number")

students = ("Alice" , "Bob" , "Charlie")

students = tuple(["Siberian"] + list(students)[1:])
print(students)

print("-----------------------------")

# enumerate()
students = ("Alice" , "Bob" , "Charlie" , "Siberian")
for index, value in enumerate(students , start=20):
     print(f"{index} : {value}")