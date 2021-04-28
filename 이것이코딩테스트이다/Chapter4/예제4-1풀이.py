import time
N = int(input())
routes = input().split()
start_time = time.time()

x, y = 1, 1

# L R U D에 따른 좌표 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for i in routes:
    nx = x + dx[move_type.index(i)]
    ny = y + dy[move_type.index(i)]

    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x = nx
    y = ny
end_time = time.time()

print("move_time : ", end_time - start_time)
print(x, y)
