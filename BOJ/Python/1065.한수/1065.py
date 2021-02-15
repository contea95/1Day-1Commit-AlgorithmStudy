def hansu(a):
    if a < 100:
        cnt = a
    else:
        cnt = 99
        for i in range(100, a+1):
            if i == 1000:
                break
            if (i % 10) - (i//10 % 10) == (i//10 % 10)-(i//100):
                cnt += 1
    return cnt


a = int(input())

print(hansu(a))
