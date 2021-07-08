def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    # 중간점보다 찾는 값이 작은 경우
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점보다 찾는값이 큰 경우
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진탐색 시작
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("찾는 값이 존재하지 않습니다.")
else:
    print((result + 1), "번째에 존재합니다.")
