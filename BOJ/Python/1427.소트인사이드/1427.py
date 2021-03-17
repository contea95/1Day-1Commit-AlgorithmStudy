N = list(map(int, input()))

sorted_N = sorted(N, reverse=True)

for i in sorted_N:
    print(i, end='')
