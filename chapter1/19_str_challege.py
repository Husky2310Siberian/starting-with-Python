# H
# ee
# lll
# llll
# ooooo
message = "Factory"

for i in range(len(message)):
    print(message[i] * (i + 1))
print()

# Hello
# H****
# ll***
# llll*
# ooooo

message = "Factory"
for i in range(len(message)):
    print(message[i] * (i + 1), end= "*" * (len(message) -1 - i) + "\n")
print()
