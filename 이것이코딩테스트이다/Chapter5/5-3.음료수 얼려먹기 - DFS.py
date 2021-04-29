N, M = map(int, input().split())
maps = []
visited = []
# 맵 입력
for i in range(N):
    maps.append(list(map(int, input())))
    visited.append([False] * M)

# True : 조건에 맞는 것 ( map = 0이고 visited = False)
# Fasle : 해당 좌표가 이상하거나, 한번 방문했을 때


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if maps[x][y] == 0 and not visited[x][y]:
        # 방문처리 후 재귀
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
