N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
a = sorted(numbers)

loop_cnt = M // (K+1)
remain = M % (K+1)
print(loop_cnt, remain)
ans = 0
ans = (a[-1] * K + a[-2]) * \
    loop_cnt + a[-1] * remain
print(ans)
