a = input()
b = list(a)
c = [-1 for i in range(26)]


for i in range(len(a)):
    if c[ord(b[i])-97] == -1:
        c[ord(b[i])-97] = i
    else:
        pass

for i in range(len(c)):
    print(c[i], end=' ')
