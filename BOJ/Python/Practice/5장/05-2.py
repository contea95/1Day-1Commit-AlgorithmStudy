class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculatior(Calculator):
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        if(self.value > 100):
            self.value = 100  # 여기에 ==을 붙여서 잘못됨.


cal = MaxLimitCalculatior()
cal.add(50)
cal.add(60)

print(cal.value)
