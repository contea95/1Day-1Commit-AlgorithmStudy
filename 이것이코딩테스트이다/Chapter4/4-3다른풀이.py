pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - ord('a') + 1
cnt = 0
steps = [(-2, -1), (-1, -2), (-2, 1), (-1, 2),
         (2, -1), (1, -2), (2, 1), (1, 2)]

for i in steps:
    if row - int(i[1]) < 1 or row - int(i[1]) > 8 or col - int(i[0]) < 1 or col - int(i[0]) > 8:
        continue
    cnt += 1

print(cnt)
