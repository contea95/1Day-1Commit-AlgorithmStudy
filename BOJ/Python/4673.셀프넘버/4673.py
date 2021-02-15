def self_num(a):
    sum_list = []
    origin_num = a
    while a > 0:
        sum_list.append(a % 10)
        a = a//10
    result = origin_num + sum(sum_list)
    return result


b = list(range(1, 10000))

for i in range(1, 10000):
    c = self_num(i)
    if c in b:
        b.remove(c)
    else:
        pass

for i in range(len(b)):
    print(b[i])
