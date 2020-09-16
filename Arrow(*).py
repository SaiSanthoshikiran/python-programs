#" arrow pattern "
def pattern(n):
    for i in range(1,n):
        for j in range(0,i):
            print(' ',end="")
        for k in range(0,i):
            print('*',end="")
        print()
    for i in range(0,n):
        for j in range(0,n-i):
            print(' ',end="")
        for k in range(0,n-i):
            print('*',end="")
        print()
    
n=int(input('n'))
pattern(n)

----------------------->>

def pattern(n):
    for i in range(1,n):#1,2
        for j in range(n-i,0,-1):#3,2
            print(' ',end="")
        for k in range(n-i):
            print('*',end="")
        print()
    for i in range(0,n):
        for j in range(0,i):#3,2
            print(' ',end="")
        for k in range(i):
            print('*',end="")
        print()
n=int(input('n'))
pattern(n)
