import os

a = os.popen("pwd")  # popen 은 시스템 명령어를 실행한 결과값을 읽기 모드로 리턴
print(a.read())
