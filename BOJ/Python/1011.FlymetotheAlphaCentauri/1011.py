'''import sys
t = int(sys.stdin.readline())
count = []
for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    list1 = [0]
    list2 = [0]
    add_count = 1
    odd_check = 0
    while 1:
        if odd_check == 0:
            list2.append(add_count)
            if sum(list1) < distance and distance <= sum(list2):
                break
            list1 = list2[:]
            odd_check = 1
        elif odd_check == 1:
            list2.append(add_count)
            if sum(list1) < distance and distance <= sum(list2):
                break
            list1 = list2[:]
            add_count += 1
            odd_check = 0
    count.append(len(list2)-1)

for j in count:
    print(j)
'''

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    num = 1
    while True:
        if num ** 2 <= distance < (num + 1) ** 2:
            break
        num += 1
    if num ** 2 == distance:
        print((num * 2) - 1)
    elif num ** 2 < distance <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)
