a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if c - b <= 0:
    print("-1")
else:
    print((a // (c-b)) + 1)
