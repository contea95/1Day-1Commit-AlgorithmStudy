'''
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n = input()

cnt = len(n)
for i in a:
    if i in n:
        if len(i) == 3:
            cnt -= 2
        else:
            cnt -= 1

print(cnt)
'''


a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n = input()

cnt = len(n)
for i in a:
    cnt -= n.count(i)

print(cnt)
