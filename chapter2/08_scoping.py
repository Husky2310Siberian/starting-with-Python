import random

random_numbers = []
random_number = []

for _ in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)

# random_numbers.sort()
print(random_numbers)

for num in random_numbers:
    if num % 2 == 0:
        even = num

print(f"The last number in list is {num}")
print(f"The last 'even' in list is {even}")
