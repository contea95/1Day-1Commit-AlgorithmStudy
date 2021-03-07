N, M = map(int, input().split())
check_list = []
for i in range(N):
    check_list.append(input())

change_min = []

for i in range(N-7):
    for j in range(M-7):
        min_change_start_W = 0
        min_change_start_B = 0
        for k in range(8):
            for l in range(8):
                if (l+k) % 2 == 0:
                    if check_list[i+k][j+l] != 'W':
                        min_change_start_W += 1
                    elif check_list[i+k][j+l] != 'B':
                        min_change_start_B += 1
                if (l+k) % 2 == 1:
                    if check_list[i+k][j+l] != 'B':
                        min_change_start_W += 1
                    elif check_list[i+k][j+l] != 'W':
                        min_change_start_B += 1
        change_min.append(min_change_start_B)
        change_min.append(min_change_start_W)

print(min(change_min))
