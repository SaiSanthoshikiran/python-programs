num=int(input('n'))
k=[[0 for x in range(num)]for y in range(num)]
n=1
L=0
h=num-1
count=int((num+1)/2)
for i in range(count):
    for j in range(L,h+1):
        k[i][j]=n
        n=n+1
    for j in range(L+1,h+1):
        k[j][h]=n
        n=n+1
    for j in range(h-1,L-1,-1):
        k[h][j]=n
        n=n+1
    for j in range(h-1,L,-1):
        k[j][L]=n
        n=n+1
    L=L+1
    h=h-1
    
for i in range(num):
    for j in range(num):
        print(k[i][j],end="\t")
    print()


