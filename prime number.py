n=int(input('enter value'))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print('prime num is',n)
else:
    print(n,'not prime')
##---------------->>
#"to the list of prime num in a given range"
import math
s=int(input('enter  start value'))
e=int(input('enter ending value'))
for i in range (s,e+1):
    for j in range (2,abs(int(math.sqrt(i))+1)):
        if i%j==0:
            break
    else:
        print(i,end=" ")
            
