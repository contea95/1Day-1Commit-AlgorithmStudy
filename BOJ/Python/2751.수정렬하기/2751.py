import math

N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
# 합병정렬
'''
def mergeSort(array):
    if len(array) < 2:
        return array
    pivot = math.floor(len(array)/2)
    left = array[:pivot]
    right = array[pivot:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

result = mergeSort(a)
'''
'''
# 합병정렬 통과용
result = sorted(a)
'''
# 힙 정렬


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2*index + 1
    right_index = 2*index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap(unsorted):
    n = len(unsorted)
    for i in range(n//2 - 1, -1, -1):    # n//2 -1부터 0까지
        heapify(unsorted, i, n)
    for i in range(n-1, 0, -1):     # n-1 부터 1까지
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)     # 새 루트노드에 대한 힙 구성
    return unsorted


result = heap(a)

for i in result:
    print(i)
