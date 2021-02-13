cases = int(input())
percent = []
for i in range(cases):
    case = []
    upper_count = 0
    case = list(map(int, input().split()))
    stu_num = case.pop(0)
    case_per = sum(case) / stu_num
    for j in range(stu_num):
        if case[j] > case_per:
            upper_count += 1
    percent.append(round(upper_count/stu_num * 100, 3))

for list in percent:
    print("{0:.3f}%".format(list))
