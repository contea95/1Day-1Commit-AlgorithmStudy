coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피 드림")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d 주고 커피 드림" % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 주고 커피 안줌")
        print("남은 커피의 양 %d" % coffee)
    if coffee == 0:
        print("커피 없음")
        break
