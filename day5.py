#for i in range(1,-101,-1):
#   print(i)
#--------->


#------->
n=int(input('enter'))
if n%2==0:
    if 2<=n<=5:
        print('not weird')
    elif 6<=n<=20:
        print('weird')
    else:
        print('not weird')
else:
    print('weird')
