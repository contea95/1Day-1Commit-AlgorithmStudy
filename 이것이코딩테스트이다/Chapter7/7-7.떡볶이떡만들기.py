n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
result = 0

start = 0
end = max(array)
while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            sum += (end - mid)
    if sum > m:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)
