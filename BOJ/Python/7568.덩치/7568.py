N = int(input())
info_list = []
for i in range(N):
    info_list.append(list(map(int, input().split())))


for i in info_list:
    r = 1
    for j in info_list:
        if i[0] < j[0] and i[1] < j[1]:
            r += 1
    print(r, end=' ')

# 그냥 전수조사 후 키가 나보다 크고 몸무게가 나보다 큰 사람을 찾아 몇명인지 세서 등수를 정한다.
