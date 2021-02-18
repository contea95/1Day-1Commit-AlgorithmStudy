def find_layer(num):
    sum = 1
    layer = 1
    while sum < num:
        layer += 1
        sum += layer
    return layer


a = int(input())
b = find_layer(a)
c = sum(list(range(1, b)))
total = b + 1

if b % 2 == 0:  # b가 짝수면
    print("%d/%d" % ((a-c), total - (a-c)))
else:
    print("%d/%d" % (total - (a-c), (a-c)))
