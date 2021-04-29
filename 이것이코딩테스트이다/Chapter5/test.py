from collections import deque

queue = deque([[1, 2]])
queue.append([3, 4])
print(queue)
v = queue.popleft()
print(v[0], v[1])
