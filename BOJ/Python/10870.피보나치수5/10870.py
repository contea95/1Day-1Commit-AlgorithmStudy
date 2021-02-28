a = int(input())
a1 = 0
a2 = 1
sum = 0
for i in range(a):
    sum = a1+a2
    a1 = a2
    a2 = sum

print(a1)
