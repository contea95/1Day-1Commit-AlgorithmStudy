N = int(input())
a = []

for _ in range(N):
    a_input, b_input = map(str, input().split())
    a_input = int(a_input)
    a.append((a_input, b_input))

a.sort(key=lambda x: (x[0]))

for i in a:
    print(i[0], i[1])
