map_r, map_c = map(int, input().split())
pos_r, pos_c, dir = map(int, input().split())
maps = []
# 지나간 루트 기록 리스트 d
d = [[0] * map_c for _ in range(map_r)]
for _ in range(map_r):
    maps.append(list(map(int, input().split())))    # 맵 생성
mov_tile = 1
d[pos_r][pos_c] = 1  # 처음 자리 왔다 감 체크
# 북, 동, 남, 서 보는 방향 시 이동 루트(왼쪽 회전 시 북 서 남 동 순으로 움직임)
dir_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
rotate_idx = 0  # 회전 4번 제한

while True:
    dir = (dir-1) % 4  # 처음 방향에서 왼쪽으로 회전
    # 이동 좌표
    nx = pos_r + dir_list[dir][1]
    ny = pos_c + dir_list[dir][0]
    if d[nx][ny] == 0 and maps[nx][ny] == 0:  # 가보지 않았고 바다 타일이 아닌 경우
        d[nx][ny] = 1  # 갔다는 것 체크
        pos_r = nx
        pos_c = ny  # 위치 변경
        rotate_idx = 0  # 회전 인덱스 reset
        mov_tile += 1  # 타일 수 증가
        continue
    else:  # 바다타일이거나 가본 경우
        rotate_idx += 1
    if rotate_idx == 4:  # 모든 방향으로 움직일 수 없는 경우
        nx = pos_r - dir_list[dir][1]
        ny = pos_c - dir_list[dir][0]
        if maps[nx][ny] == 0:   # 뒤로 갈 수 있으면
            pos_r = nx
            pos_c = ny
        else:   # 뒤로 갔는데 바다인 경우
            break
        rotate_idx = 0

print(mov_tile)

''' test case
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

4 4
1 1 0
1 1 1 1
1 0 1 1
1 1 1 1
1 1 1 1

4 4
1 1 0
1 1 1 1
1 0 0 1
1 0 0 1
1 1 1 1

5 5
2 2 0
1 1 1 1 1
1 0 1 1 1
1 0 0 0 1
1 1 1 0 1
1 1 1 1 1

5 5
3 3 1
1 1 1 1 1
1 0 1 1 1 
1 0 0 0 1
1 1 0 0 1
1 1 1 1 1
'''
