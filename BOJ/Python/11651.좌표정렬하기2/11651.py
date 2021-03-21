N = int(input())

a = []

for i in range(N):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key=lambda x: (x[1], x[0]))


for j in a:
    print(j[0], j[1])
