def solution(nums):
    answer = 0
    num = len(set(nums))
    count = len(nums) / 2
    if num >= count:
        answer = count
    else:
        answer = num

    return answer
