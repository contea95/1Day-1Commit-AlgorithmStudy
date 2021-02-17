a = int(input())
b = []
for i in range(a):
    b.append(list(map(str, input().split())))

for j in range(a):
    for k in range(len(b[j][1])):
        print(b[j][1][k]*int(b[j][0]), end='')
    print('\n', end='')
