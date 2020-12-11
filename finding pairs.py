n=[4,2,1,3,5]
k=2
for i in range(len(n)):
    if((n[i-1]+n[i])%2)==0:
        print(n[i-1],n[i])
        
OUTPUT:
4 2
1 3
3 5
