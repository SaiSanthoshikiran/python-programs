n=int(input("enter the value"))
for i in range (0,n+1):
    for j in range  (i):
        print("!",end="")
    print() 
 
[#output:
#enter the value5
!
!!
!!!
!!!!
!!!!!]
------------->>

n=int(input("number"))

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
#----------->>
n=[10,8,17,0,13]
for i in n:
    for j in range (len(n)):
        print(chr(i+65),end=" ")
    print()
#OUTPUT:
##K K K K K 
## I I I I I 
##  R R R R R 
##A A A A A 
##N N N N N 
