array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지고 있으면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]  # 분할 왼쪽 부분 정리
    right_side = [x for x in tail if x > pivot]  # 분할 오른쪽 부분 정리
    # 분할 후 왼쪽 부분과 오른쪽 부분 정렬하고 피벗을 붙여 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
