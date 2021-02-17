def group_word(word, cnt):
    length = len(word)
    checker = []
    for i in range(length):
        if not checker:  # 리스트가 비어있을 때, 즉 처음에만
            checker.append(word[i])
            idx = 0
        elif word[i] == checker[idx]:
            pass
        elif word[i] != checker[idx]:
            idx += 1
            checker.append(word[i])
    if len(set(checker)) == len(checker):
        cnt += 1
    return cnt


a = int(input())
b = []
cnt = 0
for j in range(a):
    b.append(input())

for k in b:
    cnt = group_word(k, cnt)

print(cnt)
