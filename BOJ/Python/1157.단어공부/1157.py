'''
a = input().upper()

b = {}
c = []
for i in range(len(a)):
    if a[i] in b:
        b[a[i]] += 1
    else:
        b[a[i]] = 1

for key, value in b.items():
    if value == max(b.values()):
        c.append(key)

if len(c) != 1:
    print("?")
else:
    print(c[0])
'''

n = input()
n = n.upper()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []

for i in alpha:
    result.append(n.count(i))
if result.count(max(result)) > 1:
    print("?")
else:
    print(alpha[result.index(max(result))])
