print("Nested loops in Python")

for i in range(1,11):
    for j in range (1,3):
        print(f"{i} * {j} = {i * j}" , end=" | ")
    print()
print()