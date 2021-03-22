N = int(input())

a = []

for _ in range(N):
    a.append(input())


result = sorted(sorted(set(a)), key=lambda x: len(x))

for i in result:
    print(i)
