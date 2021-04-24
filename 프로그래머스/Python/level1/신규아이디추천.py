def solution(new_id):
    answer = new_id
    answer_replace = " "
    answer = answer.lower()  # 1. 소문자화

    for i in answer:  # 2.빼기
        if ord(i) in range(97, 123):
            answer_replace += i
            continue
        elif ord(i) in range(48, 58):
            answer_replace += i
            continue
        elif ord(i) == 46:
            if ord(answer_replace[-1]) == 46:  # 3. 연속된 . 빼기
                continue
            answer_replace += i
            continue
        elif ord(i) in (45, 95):
            answer_replace += i
            continue
        else:
            continue

    answer_list = list(answer_replace[1:])

    if len(answer_list) > 0 and answer_list[0] == '.':  # 4. 처음, 끝 . 제거
        answer_list.pop(0)
    if len(answer_list) > 0 and answer_list[-1] == '.':
        answer_list.pop(-1)
    if len(answer_list) == 0:
        answer_list = ["a"]
    if len(answer_list) > 15:
        answer_list = answer_list[:15]
        if answer_list[-1] == '.':
            answer_list.pop(-1)
    elif len(answer_list) < 3:
        for i in range(3-len(answer_list)):
            answer_list.append(answer_list[-1])
    return "".join(answer_list)


print(solution('.aa-.'))
