N = int(input())
M = list(map(int, input().split()))

cnt = 0

for i in M:
    if i == 1:
        continue
    if i == 2:
        cnt += 1
    for j in range(2, i):
        if i / j == i // j:
            break
        elif j == i-1:
            cnt += 1

print(cnt)
