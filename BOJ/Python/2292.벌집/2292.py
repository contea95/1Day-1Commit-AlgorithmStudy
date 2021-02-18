def find_num(goal):
    sum = 1
    mul = 1
    while sum < goal:
        sum = sum + 6 * (mul)
        mul += 1
    return mul


goal = int(input())
print(find_num(goal))
