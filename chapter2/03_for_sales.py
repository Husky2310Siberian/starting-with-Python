# List of fruits
fruits = ["Banana" , "Apple" , "Mango" , "Grapes"]

# fruits we want to check
fruit_to_ckeck = "Banana"

for fruit in fruits:
    if fruit == fruit_to_ckeck:
        print(f"{fruit_to_ckeck} is in list")
        break
else: # in for-else , else implimented when loop is correct, without interrupted by break
    print(f"{fruit_to_ckeck} is not in list")

print("-------dynamic-----")

if fruit_to_ckeck in fruits:
    print(f"{fruit_to_ckeck} is in list")
else:
    print(f"{fruit_to_ckeck} is not in list")

print(f"{fruit_to_ckeck} is {'in' if fruit_to_ckeck in fruits else 'not in'} the list")