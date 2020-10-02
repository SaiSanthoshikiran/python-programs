r=int(input("enter no.of rows"))
c=int(input("enter no.of columns"))
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
    

