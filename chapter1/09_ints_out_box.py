a = 10
b = 20

result = a + b

print(f"{a} + {b} = {result}")

print(f"Type(a) : {type(a)}")
print(f"Type(b) : {type(b)}")

print(f"Type(result) : {type(result)}")

magic_result = a.__add__(b)

print(f"Magic result -> {a} + {b} = {magic_result}")