##"if n=125  then divisors are 1 5 25 125  mid values(5,25)--5+25=30 , 1*1+2*2+5*5=30 -->>>>true"
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
