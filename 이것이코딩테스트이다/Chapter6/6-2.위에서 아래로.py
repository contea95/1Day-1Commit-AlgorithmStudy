n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

array = sorted(numbers, reverse=True)

for i in array:
    print(i, end=" ")
