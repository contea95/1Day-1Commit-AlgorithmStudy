def solution(answers):
    answer = []
    d = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    c = [0, 0, 0]
    for index in range(len(answers)):
        if d[0][index % 5] == answers[index]:
            c[0] += 1
        if d[1][index % 8] == answers[index]:
            c[1] += 1
        if d[2][index % 10] == answers[index]:
            c[2] += 1

    for index, value in enumerate(c):
        if value == max(c):
            answer.append(index + 1)
    return answer


print(solution([1, 3, 2, 4, 2]))
