
count = int(input())

result = list(map(int, input().split()))
min = result[0]
max = result[0]

for i in result:
    if min > i:
        min = i
    if max < i:
        max = i

print(min, max)

# 아래는 다른 곳 참고

'''
count = int(input())

b = list(map(int, input().split()))

print('{} {}'.format(min(b), max(b)))
'''
