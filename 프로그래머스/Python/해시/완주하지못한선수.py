import collections


def solution(participant, completion):
    answer = ''
    p = participant
    c = completion
    p.sort()
    c.sort()
    for i in range(len(p)):
        if i == len(p)-1:
            answer = p[i]
            break
        if p[i] != c[i]:
            answer = p[i]
            break
    return answer

################################################


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
