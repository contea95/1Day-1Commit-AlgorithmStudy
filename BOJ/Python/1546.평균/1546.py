a = int(input())
b = list(map(int, input().split()))

M = max(b)
c = []


def fix_score(lists):
    for num in lists:
        c.append(num/M*100)


fix_score(b)
print(sum(c)/a)
