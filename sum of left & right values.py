n=[-7,1,5,2,-4,3,0]
for i in range(len(n)):
    c=0
    for j in range(0,i):
        c+=n[j]
    b=0
    for k in range(i+1,len(n)):
        b+=n[k]
    if c==b:
        print(n[i])
    
