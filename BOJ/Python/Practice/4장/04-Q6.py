def file_open():
    a = input("내용 입력 : ")
    f = open("test.txt", 'a')
    f.write(a + "\n")
    f.close()


def file_open2():
    with open("test2.txt", 'a') as f:
        f.write(input("내용 입력 : "))


file_open()
file_open2()
