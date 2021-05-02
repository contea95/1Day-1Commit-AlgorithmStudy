array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 겹쳐졌을 때
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:  # 겹쳐지기 전까지 반복
        # 왼쪽부터 끝까지 피벗보다 큰 데이터를 찾음
        # 만약 피벗보다 작으면 left + 1
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽부터 처음까지 피벗보다 작은 데이터를 찾음
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 겹쳐졌다면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽부분, 오른쪽부분 다시 반복
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
