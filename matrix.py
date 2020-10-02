r=int(input("enter no.of rows="))
c=int(input("enter no.of columns="))
matrix=[]
for i in range(1,r+1):
    a=[]
    for j in range (1,c+1):
        j=int(input("enter the nnumber"+str(i)+str(j)+" "))
        a.append(j)
    print()
    matrix.append(a)

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
    
OUTPUT:
enter no.of rows2
enter no.of columns2
enter the nnumber11 1
enter the nnumber12 1

enter the nnumber21 2
enter the nnumber22 2

1 1 
2 2 
