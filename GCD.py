##import math
##s=int(input('enter  start value'))
##e=int(input('enter ending value'))
##for i in range (s,e+1):
##    for j in range (2,abs(int(math.sqrt(i)))):
##        if i%j==0:
##            break
##        else:
##            

n=int(input("enter the range"))
a=0
b=1
for i in range(0,2):
    print(i,end=" ")
for j in range (0,n+1):
    c=a+b
    a=b
    b=c
    print(b,end=" ")
