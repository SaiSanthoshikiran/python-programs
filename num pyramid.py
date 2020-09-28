n=int(input('no.of rows='))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()

output:
no.of rows=4
   1
  212
 32123
4321234
