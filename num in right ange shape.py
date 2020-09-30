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

