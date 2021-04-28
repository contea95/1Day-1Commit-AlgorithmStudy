import time
N = int(input())
route = list(map(str, input().split()))
start_time = time.time()
x, y = 1, 1

for i in route:
    if i == 'R':
        if y == N:
            continue
        y += 1
    elif i == 'L':
        if y == 1:
            continue
        y -= 1
    elif i == 'U':
        if x == 1:
            continue
        x -= 1
    elif i == 'D':
        if x == N:
            continue
        x += 1
    else:
        break
end_time = time.time()
print("move_time : ", end_time - start_time)
print(x, y)
