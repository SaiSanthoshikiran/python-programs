a=[1,2,3,0,3,0,2,0]
c=0
for i in range (len(a)):
    if a[i]!=0:
        m=a[i]
        a[i]=a[c]
        a[c]=m
        c+=1
print(a)

#-------------------->>

a=[1,2,3,0,3,0,2,0]
for i in range(len(a)):
    if a[i]==0:
        a.pop(i)
        a.append(0)
print(a)

##OUTPUT:
##[1, 2, 3, 3, 2, 0, 0, 0]
##
##
