d={}
d2={}
n=int(input('no.of.students:'))
s=int(input('no.of subjects:'))
l=[]
for i in range(n):
    name=input('name:')
    m=list(map(int,input('marks:').split()))
    d[name]=m
    c=0
    for j in m:
        c=c+j
        l.append(c)
        d2[name]=l
m=max(l)

print("Intial list:",d)
print('max value:',d2)

        
