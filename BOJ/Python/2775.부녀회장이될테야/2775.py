case = int(input())
sum = []

for i in range(case):
    k = int(input())  # 층
    n = int(input())  # 호
    zero_floor = [x for x in range(1, n+1)]
    for j in range(k):
        for l in range(1, n):
            zero_floor[l] += zero_floor[l-1]
    sum.append(zero_floor[-1])

for i in range(len(sum)):
    print(sum[i])
