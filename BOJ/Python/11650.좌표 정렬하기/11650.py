N = int(input())

a = {}
for i in range(N):
    tmp = []
    x_input, y_input = map(int, input().split())
    if x_input in a:
        tmp = a[x_input]
        tmp.append(y_input)
        tmp.sort()
        a[x_input] = tmp
    else:
        a[x_input] = [y_input]

sorted_a_key = sorted(a.items())

for i in sorted_a_key:
    for j in i:
        if str(type(j)) == "<class 'int'>":
            a_type = j
        elif str(type(j)) == "<class 'list'>":
            for k in j:
                print(a_type, k)
