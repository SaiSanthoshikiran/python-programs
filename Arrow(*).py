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

OUTPUT:
n4
 *
  **
   ***
    ****
   ***
  **
 *

----------------------->>
#reverse direction tried
def pattern(n):
    for i in range(1,n):#1,2
        for j in range(n-i,0,-1):#3,2
            print(' ',end="")
        for k in range(n-i):
            print('*',end="")
        print()
    for i in range(1,n+5):
        print("="*2,end="")
    for i in range(0,n):
        for j in range(0,i):#3,2
            print(' ',end="")
        for k in range(i):
            print('*',end="")
        print()
n=int(input('n'))
pattern(n)

OUTPUT:
n4
   ***
  **
 *
==================
 *
  **
   ***

-------------------------->>
def arrow(n):
    for i in range(n):
        for j in range(0,i+5):
            print(' ',end="")
        for j in range(1):
            print('*',end="")
        print()
    for i in range(0,n+5):
        print('*',end="")
    print()
    for i in range(n):
        for j in range(0,n-i+3):
            print(' ',end="")
        for j in range(1):
            print('*',end="")
        print()
    
n=int(input('n'))
arrow(n)

OUTPUT:
     *
      *
       *
        *
*********
       *
      *
     *
    *


