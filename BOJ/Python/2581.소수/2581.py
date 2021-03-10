N = int(input())
M = int(input())

decimal_list = []

for i in range(M - N + 1):
    num = N + i
    if num == 1:
        continue
    elif num == 2:
        decimal_list.append(2)
        continue
    else:
        for j in range(2, num):
            if num/j != num//j:
                if j == num-1:
                    decimal_list.append(num)
            else:
                break

if len(decimal_list) > 0:
    print(sum(decimal_list))
    print(min(decimal_list))
else:
    print(-1)
