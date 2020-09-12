##"a number is a sastry number if n concatenated with n+1 gives a perfect square---n=183,n+1=184-->>183+184=183184=428 "
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
    
--------------------------->>
    
n=int(input('n='))
str1=str(n)+str(n+1)
k=int(str1)**0.5
if(k.is_integer()):
    print('yes')
else:
    print('no')
    
------------------->>>

