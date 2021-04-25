N, M = map(int, input().split())
cards = []
min_row = []
for i in range(N):
    cards.append(list(map(int, input().split())))
    min_row.append(min(cards[i]))
print(max(min_row))
