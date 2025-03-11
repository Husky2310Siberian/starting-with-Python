# populate a list
ages = [19 , 23 , 34 , 55]

print("Initial list of ages" , ages)

print("\nIterating with index and value:")
for index , value in enumerate(ages):
    print(f"index : {index}  --> value : {value}")

print("\nIterating with enchanced for:")
for age in ages:
    print(age , end=" , ")
print()