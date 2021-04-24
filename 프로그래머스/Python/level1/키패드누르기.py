def solution(numbers, hand):
    answer = ''
    lp = [3, 0]
    rp = [3, 2]
    for i in numbers:
        if i == 0:
            i = 11
        num_row = (i-1) // 3
        num_col = (i-1) % 3
        print("row, col : ", num_row, num_col)
        diff_lp = abs(lp[0] - num_row) + abs(lp[1] - num_col)
        diff_rp = abs(rp[0] - num_row) + abs(rp[1] - num_col)
        print(diff_lp, diff_rp)
        if num_col == 0:
            answer += "L"
            lp = [num_row, num_col]
            continue
        elif num_col == 2:
            answer += "R"
            rp = [num_row, num_col]
            continue
        elif diff_lp < diff_rp:
            answer += "L"
            lp = [num_row, num_col]
            continue
        elif diff_lp > diff_rp:
            answer += "R"
            rp = [num_row, num_col]
            continue
        else:
            if hand == "right":
                answer += "R"
                rp = [num_row, num_col]
                continue
            elif hand == "left":
                answer += 'L'
                lp = [num_row, num_col]
                continue
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
