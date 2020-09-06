
n=int(input("enter a number"))
m=int(input("enter a number"))
if n<m:
    small=n
else:
    small=m
for i in range(1,small+1):
    if (n%i==0 and m%i==0):
        gcd=i
        print('multiplicants',i)
print("gcd is",gcd)

##-------------->>

n=int(input("enter a number"))
m=int(input("enter a number"))
i=1
gcd=1
while i<=min(n,m):
    if n%i==0 and m%i==0:
        gcd=i
    i+=1
print(gcd)
