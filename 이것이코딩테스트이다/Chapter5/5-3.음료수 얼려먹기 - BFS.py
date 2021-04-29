from collections import deque


def ice(maps, visited, x, y):
    # 상 하 좌 우
    mx = [0, 0, -1, 1]
    my = [-1, 1, 0, 0]
    queue = deque([[x, y]])
    while queue:
        n = queue.popleft()
        nx, ny = n[0], n[1]
        for i in range(4):
            mv_x = nx + mx[i]
            mv_y = ny + my[i]

            if mv_x >= 0 and mv_y >= 0 and mv_x < len(maps) and mv_y < len(maps[0]):
                if maps[mv_x][mv_y] == 0 and not visited[mv_x][mv_y]:
                    queue.append([mv_x, mv_y])
                    visited[mv_x][mv_y] = True


N, M = map(int, input().split())
maps = []
visited = []
cnt = 0
for i in range(N):
    maps.append(list(map(int, input())))
    visited.append([False] * M)
    # 배열 선언 시 [False] * M] * N으로 해버리면
    # 그냥 똑같은 한 줄의 배열이 주소로 복사됨
    # 이렇게 되면 0,0을 False -> True가 되어버리면
    # 1,0 2,0 3,0 ... 이 전부 True가 되어버린다.
    # 얕은 복사? 참고 https://codingdog.tistory.com/entry/파이썬-2차원-배열-초기화-얕은-복사만-조심하면-된다
for i in range(N):
    for j in range(M):
        # print("check : ", i, j)
        # 타일이 0이고, 방문한 적이 없다면 좌표 주변 탐색
        if maps[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            ice(maps, visited, i, j)
            cnt += 1

print(cnt)
