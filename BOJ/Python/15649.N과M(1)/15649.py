N, M = map(int, input().split())
check = [0] * (N+1)  # 1부터 N까지의 자연수 설정, 사용했다 안했다의 체크용
result = [0] * M    # 출력 결과를 저장하는 리스트


def recursive(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=" ")
        print()
        return

    for i in range(1, n+1):  # 수를 탐방하면서 계속 재귀를 돌림
        if check[i] == 1:   # i가 이미 사용된 수라면
            continue        # for문의 i를 +1시키고 다시 시작
        check[i] = 1        # check[i]를 1로 바꿔 사용했다는 것을 표시
        result[index] = i   # result의 위치에 i를 대입
        recursive(index+1, n, m)  # index를 1늘리고 재귀 시작
        # 백트래킹은 스택구조라서 위의 index == m 조건이 만족되고 출력되면 사용했던 나머지를 0으로 돌림
        check[i] = 0


recursive(0, N, M)
