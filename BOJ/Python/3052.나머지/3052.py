a = []
count = {}
for i in range(10):
    a.append((int(input())) % 42)

for i in a:
    try:
        count[i] += 1
    except:
        count[i] = 1

print(len(count))
