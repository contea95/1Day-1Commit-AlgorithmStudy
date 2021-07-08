n = int(input())
array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for j in x:
    if array[j] != 0:
        print("yes", end=" ")
    else:
        print("no", end=" ")
