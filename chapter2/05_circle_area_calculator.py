# Calculates the area of a circle based on the radius entered by the user
from math import pi

r = float(input("Please input the radius of circle\n"))

area = pi * r * r

print("The area for given r = ", r ," is " , area)