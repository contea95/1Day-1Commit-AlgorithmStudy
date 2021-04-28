pos = input()
col, row = pos[0], pos[1]
cnt = 0
col_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row_table = ['1', '2', '3', '4', '5', '6', '7', '8']
check_list = [-2, -1, 1, 2]

# print(row_table.index(row))

for i in check_list:
    if int(row_table.index(row)) + i < 0 or int(row_table.index(row)) + i > 7:
        continue
    for j in check_list:
        if i == j or i == -j:
            continue
        if int(col_table.index(col)) + j < 0 or int(col_table.index(col)) + j > 7:
            continue
        cnt += 1

print(cnt)
