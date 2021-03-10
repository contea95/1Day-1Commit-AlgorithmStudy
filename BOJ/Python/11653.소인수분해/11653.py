N = int(input())

decimal_split = []

while True:
    if N == 1:
        break
    if N == 2:
        decimal_split.append(2)
        break
    else:
        for i in range(2, N):
            if N / i == N // i:  # 소수가 아닐 때
                decimal_split.append(i)
                N = N // i
                break
            elif N/i != N//i:
                if i == N-1:
                    decimal_split.append(i+1)
                    N = 1
                    break

for i in decimal_split:
    print(i)
