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

OUTPUT:
no.of students:2
enter student name:k
enter subject marks:2 2 2
enter student name:r
enter subject marks:3 3 3
{'k': [6], 'r': [9]}
