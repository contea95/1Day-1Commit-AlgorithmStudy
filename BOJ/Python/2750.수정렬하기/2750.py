N = int(input())
sort_list = []

for i in range(N):
    sort_list.append(int(input()))
# 삽입정렬
'''
for i in range(1, len(sort_list)):
    j = i - 1
    key = sort_list[i]
    while sort_list[j] > key and j >= 0:
        sort_list[j+1] = sort_list[j]
        j = j-1
    sort_list[j+1] = key
'''
# 거품 정렬
for i in range(len(sort_list) - 1):
    for j in range(len(sort_list) - (i+1)):
        if sort_list[j] > sort_list[j+1]:
            tmp = sort_list[j+1]
            sort_list[j+1] = sort_list[j]
            sort_list[j] = tmp

for i in sort_list:
    print(i)
