def stars(n):
    matrix = []
    for i in range(len(n) * 3):
        if int(i / len(n)) == 1:
            matrix.append(n[i % len(n)] + ' ' * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))


n = int(input())
k = 0
while n != 3:
    n = int(n/3)
    k += 1  # k는 재귀 반복 횟수

star = ["***", "* *", "***"]
for i in range(k):
    star = stars(star)
for i in star:
    print(i)
