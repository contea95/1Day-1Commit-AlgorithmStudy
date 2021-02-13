a = int(input())
b = []
for i in range(a):
    b.append(input())

result = []

for s in b:
    tot_score = 0
    score = 0
    length = len(s)
    for j in range(length):
        if s[j] == 'O':
            score += 1
            tot_score += score
        elif s[j] == 'X':
            score = 0
            tot_score += score
    result.append(tot_score)

for i in result:
    print(i)
