N, M = map(int, input().split())
check = [0] * (N+1)
result = [0] * M


def recursive(index, pre_idx, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=" ")
        print()
        return()

    for i in range(pre_idx, n+1):
        if check[i] == 1:
            continue
        check[i] = 1
        result[index] = i
        recursive(index + 1, i + 1, n, m)
        check[i] = 0


recursive(0, 1, N, M)
