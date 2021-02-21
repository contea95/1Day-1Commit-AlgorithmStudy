n = int(input())
a = n // 5
b = 0
if n == 4 | n == 7:
    print(-1)
else:
    while a >= 0:
        if a == n/5:
            break
        elif (n-(5*a)) % 3 == 0:
            b = int((n-(5*a)) / 3)
            break
        else:
            a -= 1

    print(a + b)
