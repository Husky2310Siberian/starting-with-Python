name = input("Please insert your name: ").capitalize()

is_student = input("Are you a student ? (yes/no): ").lower() == "yes"

print(f"{name}")
print(f"is a student : {is_student}")

if is_student:
    print("You are a student")
else:
    print("you are not a student")