message = "Hello World"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])

print(f"Number of letters on word {message} is : {len(message)}")

for char in message: 
    print(char , end=" ")
print()

for i in range(10):
    print(i , end=" ")
print()

for i in range(len(message)):
    print(message[i] , end=" ")
print()

print(type(range(10)))

# Range normally works: 
# defalt start --> 0 (inclusive)
# default step --> 1
# default point --> stop -1 (exclusive)
for i in range (1, 10 , 3):
    print(i , end=" , ")
print()