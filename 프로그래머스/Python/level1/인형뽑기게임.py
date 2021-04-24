def solution(board, moves):
    answer = 0
    row = len(board)
    col = len(board[0])
    basket = [0]
    count = 0
    for i in moves:
        for j in range(col):
            if board[j][i-1] == 0:
                continue
            else:
                basket.append(board[j][i-1])
                if basket[-1] == basket[-2]:
                    basket.pop(-1)
                    basket.pop(-1)
                    count += 2
                board[j][i-1] = 0
                break
    answer = count
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
    4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
