M, N = list(map(int, input().split()))

prime = list(range(1000001))
list_num = 1000001
prime[1] = 0
for i in range(2, int(list_num**0.5) + 1):
    if prime[i] != 0:  # 수가 소수이면
        for j in range(2*i, list_num, i):  # step i 만큼 뛰면서 0으로 만든다.
            prime[j] = 0


for k in range(M, N+1):
    if prime[k] != 0:
        print(prime[k])

# print(list(filter(lambda x: x != 0, prime[M:N+1])))
