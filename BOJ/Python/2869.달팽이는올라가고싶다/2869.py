import math

a, b, v = map(int, input().split())

'''
while height < v:
    height += a
    if height >= v:
        break
    height -= b
    day += 1

print(day)
'''
day = math.ceil((v - a)/(a - b)) + 1

print(day)
