from os import replace


f = open("test.txt", 'r')
body = f.read()  # 읽어서 변수에 저장
f.close()

body = body.replace('java', 'python')  # 변수에 있는 문자열 변환

f = open("test.txt", 'w')  # 다시 쓰기
f.write(body)
