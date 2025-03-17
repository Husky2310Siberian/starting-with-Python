import random

random_numbers = []
random_number = []

for _ in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)

# random_numbers.sort()
print(random_numbers)

# num is defined inside the loop, but in Python, variables inside a loop do not have block scope,
# this means after the loop finishes, num will still exist in the global scope,
# storing the last randomly generated number.
for num in random_numbers:
    if num % 2 == 0:
        even = num

print(f"The last number in list is {num}")
print(f"The last 'even' in list is {even}")
