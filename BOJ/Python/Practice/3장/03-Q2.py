number = 1
result = 0
while number <= 1000:
    if number % 3 == 0:
        result = result + number
    number = number + 1
    print(result)
