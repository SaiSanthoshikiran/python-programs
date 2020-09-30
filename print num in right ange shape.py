num=int(input('num:'))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


OUTPUT:
num:4
1 
1 2 
1 2 3 
1 2 3 4

------------------------>>

num=int(input('num:'))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

OUTPIT:
num:4
1 
2 2 
3 3 3 
4 4 4 4

------------------>>

n=int(input('n:'))
for i in range(n):
    val=i+1
    dec=n-1
    for j in range(i+1):
        print(val,end=' ')
        val=val+dec
        dec=dec-1
    print()

    
OUTPUT:
n:5
1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15 
    
    
    
    
    
    
    
