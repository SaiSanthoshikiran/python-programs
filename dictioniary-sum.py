a={}
n=int(input('no.of students:'))
for i in range(n):
    k=input('enter student name:')
    v=[]
    s=list(map(int,input('enter subject marks:').split()))
    c=0
    for i in s:
        c=c+i
    v.append(c)
    a[k]=v
print(a)

        
