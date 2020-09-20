def num(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r**2
        n=n//10
    return(s)
def happy(n):
    while n>10:
        k=num(n)
        if k==1 or k==7:
            return('yes')
        else:
            n=k
    else:
        if n==1 or n==7:
            return('yes')
        else:
            return('no')
n=int(input("n="))
print(happy(n))


-------------------->>

n=int(input())
res=0
while True:
    d=n%10
    res=res+d*d
    n=n//10
    
    if res<9 and n==0:
        break
    if n==0:
        n=res
        res=0
if res==1 or res==7:
    print('happy')
else:
    print('not happy')
