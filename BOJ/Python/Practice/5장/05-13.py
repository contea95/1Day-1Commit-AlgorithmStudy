import random

a = list(range(1, 46))

result = []

for i in range(6):
    number = random.choice(a)
    result.append(number)
    a.remove(number)
result.sort()
print(result)
print(a)
