n = int(input())
stu_list = []
for _ in range(n):
    stu_list.append((input().split()))

array = sorted(stu_list, key=lambda x: x[1])

for i in array:
    print(i[0], end=" ")
