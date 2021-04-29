from collections import deque

n, m = map(int, input().split())
graph = []
visited = []
for i in range(n):
    graph.append(list(map(int, input())))
    visited.append([False] * m)


def bfs(x, y):
    step_x = [0, 0, -1, 1]
    step_y = [-1, 1, 0, 0]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + step_x[i]
            ny = y + step_y[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph


print(bfs(0, 0))
