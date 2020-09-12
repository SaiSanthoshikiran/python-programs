def  num(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r**2
        n=n//10
    return(s)
def xyz(n):
    s1=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i==n//i:
                s1+=1
            else:
                s1+=(i+n//i)
    return(s1-1-n)
def canada(n):
    return(xyz(n)==num(n))
    if canada(n):
        print('yes')
    else:
        print('no')
n=int(input('n'))
print(canada(n))
