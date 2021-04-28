n = 1234

num_sum = 0
for _ in range(len(str(n))):
    num_sum += n % 10
    n = n//10

print(num_sum)
