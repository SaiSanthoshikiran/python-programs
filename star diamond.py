def pattern(n):
    for i in range(n):
        print(("*"*(i+1)).center(2*n))
    for i in range(n-1,0,-1):
        print(("*"*(i)).center(2*n))
n=int(input("enter the num"))
pattern(n)
