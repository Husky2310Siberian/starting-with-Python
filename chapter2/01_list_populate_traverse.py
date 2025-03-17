# populate a list
ages = [19 , 23 , 34 , 55]

print("Initial list of ages: ", ages)

print("\n Iterating with index and values:")
for index , value in enumerate(ages):  # (index , value)
    print(f"index {index}, value {value}")

print("\n Iterating with enhance for")
for age in ages:
    print(age, end=" ")
print()