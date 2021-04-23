# def solution(n, lost, reserve):
#     answer = n - len(lost)

#     for i in lost:
#         if i in reserve:
#             lost.remove(i)
#             reserve.remove(i)
#             answer += 1
#             continue
#     for i in lost:
#         if i - 1 in reserve:
#             answer += 1
#             reserve.remove(i-1)
#             continue
#         elif i + 1 in reserve:
#             answer += 1
#             reserve.remove(i+1)
#             continue
#     return answer

# 위처럼 풀면 lost와 reserve를 지울 때 10, [5, 4, 3, 2, 1], [3, 1, 2, 4, 5] 조건에서
# lost에서 지웠기 때문에 4가 스킵이 되어버린다. 3이 지워지고 2가 또 스킵이 된다. 그래서 문제가 생기는 것

def solution(n, lost, reserve):
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    answer = n - len(real_lost)
    for i in real_lost:
        if i - 1 in real_reserve:
            answer += 1
            real_reserve.remove(i-1)
            continue
        elif i + 1 in real_reserve:
            answer += 1
            real_reserve.remove(i+1)
            continue
    return answer


print(solution(10, [5, 4, 3, 2, 1], [3, 1, 2, 4, 5]))

