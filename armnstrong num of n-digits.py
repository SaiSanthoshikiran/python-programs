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

