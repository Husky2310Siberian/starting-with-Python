students = ("Alice" , "Bob" , "Charlie")

print(type(students))

# iterate
for index , student in enumerate(students):
    print(f"{index} --> {student}")
print("-------------")
# enhance for
for student in students:
    print(student)

# first_student = students[0]
# second_student = students[1]
# third_student = students[2]

first_student , second_student , third_student = students

print("-------------")
print(f"first_student : {first_student}")
print(f"second_student : {second_student}")
print(f"third_student : {third_student}")


# students = ("Alice" , "Bob" , "Charlie")

students = list(students) # convert to list
students[0] = "Alec" # update the zero index
students = tuple(students) # convert to tuple

students = list(students)
print(students)