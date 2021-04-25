N, K = map(int, input().split())
cnt = 0
for i in range(25):
    if N == 1:
        break
    if N % K == 0:  # 나눠질 경우
        N = N / K
        cnt += 1
        continue
    else:  # 나눠지지 않을 경우
        N -= 1
        cnt += 1
        continue

print(cnt)
