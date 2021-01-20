def avg(*num):
    sum = 0
    for i in num:
        sum += i
    print("result : %f" % (sum / len(num)))


avg(1, 2, 3, 4)
