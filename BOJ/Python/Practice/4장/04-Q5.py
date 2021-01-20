f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()  # 파일이 쓰기모드로 open된 상태에서 읽을 수 없다.
f2 = open("test.txt", 'r')
print(f2.read())
