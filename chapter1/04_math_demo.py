import math

name = "Alice"
age = 20

print("PI=" , math.pi)

# print(name + " is " + age + " years old.")
print(name + " is " + str(age) + " years old.")

print("PI = %6.2f"  %math.pi)

print("%s is %d"  %(name , age))

print("Age is {0:2d}".format(age))
print("PI is {0:.3f}".format(math.pi))

print("{0} is {1}".format(name , age))

print("{0:*^10} : {1:<20}".format(name , age), end=".\n")

print(f"{name} is {age} years old")