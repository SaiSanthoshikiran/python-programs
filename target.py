def fun(fb,n):
    fb=[0]+fb+[0]
    c=0
    for i in range(len(fb)):
        if fb[i:i+3]==[0,0,0]:
            c+=1
            if c>=n:
                return True
            fb[i+1]=1
    return c>=n
fb=[1,0,0,0,1]
n=1
print(fun(fb,n))

OUTPUT:
True
