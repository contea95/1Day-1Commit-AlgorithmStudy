import sys


class sysnum():
    def __init__(self):
        self.sum = 0

    def argvsum(self):
        for i in range(len(sys.argv) - 1):
            self.sum += int(sys.argv[i + 1])
        print(self.sum)


a = sysnum()
a.argvsum()
