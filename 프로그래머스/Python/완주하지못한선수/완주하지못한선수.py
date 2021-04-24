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

# 조건에 여러 참가자 중 한명만 완주를 하지 못했다는 조건으로 우선 참가자와 완주자를 정렬하고
# 두 리스트를 비교 후 다른 하나만 catch해서 출력
################################################


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
