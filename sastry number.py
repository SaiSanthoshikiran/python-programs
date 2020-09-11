import math
n=int(input("n"))
m=n+1
n1=str(n)
m1=str(m)
n1+=m1
print(n1)
s=int(n1)**0.5
print(s)
c=math.ceil(s)
print("c=",c)
f=math.floor(s)
print("f=",f)
if c==f:
    print("sastry number")
else:
    print("not a sastry number")
