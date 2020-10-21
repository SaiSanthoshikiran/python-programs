#"multiplication table with limits"
n=int(input('enter the number'))
s=int(input(' enter starting num'))
r=int(input('enter range'))
if s<n:
    for i in range (s,r+1,-1):
        print(n,'*',i,'=',n*i)
else:
    for i in range(r,s-1,-1):
        print(n,'*',i,'=',n*i)
