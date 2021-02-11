'''
a = input()
b = input()
c = input()

result = int(a)*int(b)*int(c)

nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    rest = result % 10
    nums[rest] = nums[rest] + 1
    result = result // 10
    if result == 0:
        break

for i in range(10):
    print(nums[i])

'''
a = int(input())
b = int(input())
c = int(input())

k = a*b*c
k_list = list(str(k))
for i in range(10):
    k_num_count = k_list.count(str(i))
    print(k_num_count)
