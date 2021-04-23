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


print(solution(10, [5, 4, 3, 2, 1], [3, 1, 2, 5, 4]))
