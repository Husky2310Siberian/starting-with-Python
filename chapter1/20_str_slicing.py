s = "Hello World"

s1 = s[6]
print(s1)

# prints all the letters from [0] -> [4]
s2 = s[:5]
print(s2)

# prints all the letters from [6] -> [10]
s3 = s[6:]
print(s3)

s4 = s[:]
print(s4)

s5 = s[-1]
print(s5)

s6 = s[:-3]
print(s6)

s7 = s[::2]
print(s7)

# reversed
s8 = s[::-1]
print(s8)

# reversed --> in negative indexing, start point == -1, so -1 is redundancy
s9 = s[-1::-1]
print(s9)