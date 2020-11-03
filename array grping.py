l=list(map(int,input().split()))
n=int(input())
a=[]
for i in range(n):
    a.append(l[i])
    a.append(l[i+n])
print(a)
