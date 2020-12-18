n=int(input('enter value'))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print('prime num is',n)
else:
    print(n,'not prime')
##----------------------->>
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

##----------------------->>
#["prime number program using function"]
import math
def prime(n):
    for j in range (2,abs(int(math.sqrt(i))+1)):
        if n%i==0:
            break
    else:
        return(n)
n=int(input("enter a number"))
print(prime(n))
#--------------------------------------------->>
["prime number check to eliminate time limit error"]
n=int(input())
for i in range(n):
    m=int(input())
    c=0
    for j in range(2,m):
        if m%j==0:
            c+=1
            break
    if c==1:
        print("not prime")
    else:
        print("prime")
           
