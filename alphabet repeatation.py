n=int(input("enter the value"))
for i in range (0,n+1):
    for j in range  (i):
        print("!",end="")
    print()   

##
##n=int(input("number"))
##
##for i in range(1,n+1):
##    for j in range(i):
##        print("*",end="")
##    print()
#----------->>
n=[10,8,17,0,13]
for i in n:
    for j in range (len(n)):
        print(chr(i+65),end=" ")
    print()
