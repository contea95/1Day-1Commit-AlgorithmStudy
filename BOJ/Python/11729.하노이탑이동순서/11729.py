def hanoi(N, start, to, via):
    global matrix
    if N == 1:
        matrix.append(start + " " + to)
    else:
        hanoi(N-1, start, via, to)
        hanoi(1, start, to, via)
        hanoi(N-1, via, to, start)


matrix = []
N = int(input())

hanoi(N, "1", "3", "2")
print(len(matrix))
for i in matrix:
    print(i)
