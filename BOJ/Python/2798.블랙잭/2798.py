N, M = map(int, input().split())
list_num = list(map(int, input().split()))
list_len = len(list_num)
loop_num = list_len * (list_len - 1) * (list_len - 2) // 6

sum_list = []
idx_1 = 0
idx_2 = 1
idx_3 = 2
for _ in range(loop_num):
    sum = 0

    sum = list_num[idx_1] + list_num[idx_2] + list_num[idx_3]
    sum_list.append(sum)
    if idx_3 == (list_len - 1):
        if idx_2 == (list_len - 2):
            idx_1 += 1
            idx_2 = idx_1 + 1
            idx_3 = idx_1 + 2
        else:
            idx_2 += 1
            idx_3 = idx_2 + 1
    else:
        idx_3 += 1

print(max([x for x in sum_list if x <= M]))
