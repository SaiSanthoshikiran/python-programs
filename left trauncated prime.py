def prime(n):
    for i in range(2,n):
       if (n%i==0):
           break
    else:
        return(1)
n=int(input("enter the number"))
length=len(str(n))
cnt=0
while(prime(n)==1 and n>0):
    num=10**(length-1)
    n%=num
    length-=1
    if(prime(n)==1):
        cnt=1
    else:
        beak
if(cnt==1):
    print("left truncated prime")
else:
    print("not left truncated prime")
