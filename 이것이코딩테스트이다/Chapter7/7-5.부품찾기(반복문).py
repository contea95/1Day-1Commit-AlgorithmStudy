def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 데이터 개수
n = int(input())
# 데이터 입력
array = list(map(int, input().split()))
array.sort()
# 찾는 데이터 개수
m = int(input())
# 찾는 데이터 입력
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
