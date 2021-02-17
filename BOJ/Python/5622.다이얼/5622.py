a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = {}
c = '22233344455566677778889999'

for i in a:
    b[i] = int(c[a.find(i)]) + 1

n = input()
sum = 0
for j in n:
    sum += b.get(j)
print(sum)


'''
N=input()
dic={'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
ans=[]
for i in range(len(N)):
    for word in dic:
        if N[i] in word:
            ans.append(dic.get(word))
print(sum(ans))
'''
