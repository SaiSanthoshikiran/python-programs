#error
def pattern(n):
    for i in range(n):
        print(("*"*(i+1)).center(2*n))
    for i in range(n-1,0,-1):
        print(("*"*(i)).center(2*n))
n=int(input("enter the num"))
pattern(n)
---------------------->>
def pattern(n):
    for i in range(n,-n,-1):
        for j in range(1,abs(i)+1):
            print(' ',end='')
        for k in range(n,abs(i),-1):
            print('* ',end="")
        print()
n=int(input("enter the number"))
pattern(n)
