#In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself.

def length(n):
    cnt=0
    while n>0:
        n//=10
        cnt+=1
    return cnt
def armstrong(n):
    arm=0
    n1=n
    l=length(n)
    while n>0:
        rem=n%10
        arm+=rem**l
        n//=10
    if n1==arm:
        return('armstrong number')
    else:
        return('not a armstrong number')
n=int(input('enter a number'))
print(armstrong(n))

OUTPUT:
enter a number153
armstrong number
--------------------->>

def armstrong(n):
    k=1
    while n%10**k!=n:
        k+=1
    res=0
    temp=n
    while n>0:
        res+=(n%10)**k
        n//=10
    return res==temp
print(armstrong(int(input("n="))))
