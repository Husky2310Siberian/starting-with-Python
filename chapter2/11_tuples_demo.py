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