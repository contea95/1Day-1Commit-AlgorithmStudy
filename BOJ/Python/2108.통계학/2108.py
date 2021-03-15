N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
sum = sum(num)
min_num = min(num)
max_num = max(num)
avg = round(sum / N)

sort_y = sorted(num)
mid = sort_y[(N-1)//2]

my_list = [0]*(max_num - min_num + 1)
for i in num:
    my_list[i - min_num] += 1
max_my_list = max(my_list)
if my_list.count(max_my_list) > 1:  # 최빈값 겹칠 때
    res_list = list(
        filter(lambda x: my_list[x] == max_my_list, range(len(my_list))))
    freq_num = res_list[1] + min_num
else:
    freq_num = my_list.index(max_my_list) + min_num

if N != 1:
    rng = sort_y[N-1] - sort_y[0]
else:
    rng = 0

print(avg)
print(mid)
print(freq_num)
print(rng)
