a = list(input().split())

a[0] = int(a[0][::-1])
a[1] = int(a[1][::-1])

print(max(a))
