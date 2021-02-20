def room_print(h, w, n):
    floor = n % h
    room = n / h
    if floor == 0:
        floor = h
    if room == int(room):
        room -= 1
    room = int(room) + 1
    print('{0:d}{1:02d}'.format(floor, room))


n = []
case = int(input())
for i in range(case):
    n.append(list(map(int, input().split())))

for h, w, n in n:
    room_print(h, w, n)
