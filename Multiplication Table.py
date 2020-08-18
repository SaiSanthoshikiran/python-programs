
n=int(input('enter'))
s=int(input('start'))
r=int(input('range'))
if s<n:
    for i in range (s,r+1,-1):
        print(n,'*',i,'=',n*i)
else:
    for i in range(r,s-1,-1):
        print(n,'*',i,'=',n*i)
