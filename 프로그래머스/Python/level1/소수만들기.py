def solution(nums):
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum = nums[i]+nums[j]+nums[k]
                for l in range(2, sum):
                    if sum % l == 0:
                        break
                    if l == sum - 1:
                        answer += 1
    return answer


print(solution([1, 2, 3, 4]))
