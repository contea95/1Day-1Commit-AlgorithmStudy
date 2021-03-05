N = input()
len_N = len(N)

fit_list = []
if len_N > 1:
    for i in range(9+(len_N-1)*10):
        M = int(N) - i
        if M < 0:
            break
        num_sum = sum(map(int, str(M)))
        if (M + num_sum) == int(N):
            fit_list.append(M)
else:  # 1의 자리수
    if int(N) % 2 == 0:
        fit_list.append(int(N)//2)

if len(fit_list) != 0:
    print(min(fit_list))
else:
    print(0)
