##A prime number is said to be Special prime number if it can be expressed as the sum of three integer numbers: two neighboring prime numbers and 1
import math
def prime(n):
    for i in range (2,abs(int(math.sqrt(n))+1)):
        if n%i==0:
            break
    else:
        return(1)
def near_prime(n):#19 17
   n1=n-1 #18 16
   while True:
       if prime(n1):#18,17,16
           return n1
       else:
            n1-=1#17,15,14,13
n=int(input('enter a number'))
if prime(n):
    a=near_prime(n)
    b=near_prime(a)
    while True:
        if a+b+1==n:#13+17+1==19
            print(n,'is a special prime')
            break
        else:
            a=b#13
            b=near_prime(a)
            print(a,b)
        if a==2 or b==2:
            break
else:
    print("not a prime")
