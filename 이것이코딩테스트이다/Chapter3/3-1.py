def solution(money):
    answer = 0
    change = [500, 100, 50, 10]
    remain = money
    for i in change:
        answer += remain // i
        remain = remain % i
    return answer


print(solution(1260))
