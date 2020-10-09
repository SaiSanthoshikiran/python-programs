##displaying zeroes at last in o/p
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

====================================>>
n=[1,2,3,4,5]
#for i in n:
 # print(i)
#------------->>
for i in range(1,5):
  print(i)
#------------>>
n="kiran"
for i in range (len(n)):
 print(n[i],end="  ")
print()
#--------->>
n="kiran"
for i in n:
 print(i,end=" ")

==========================>>
a=[]
for i in range(5):
    if i!=2:
        a.append(i)
print(a)

#simplified code for above case

##a=[i for i in range(5) if i!=2]
##print(a)
##OUTPUT:
##[0, 1, 3, 4]

===============================>>
#o/p containg no.of less values than that particular value
n=[8,3,1,2]
l=[]
for i in range(len(n)):
    a=0
    for j in range(len(n)):
        if n[j]<n[i]:
            a+=1
    l.append(a)
print(l)

OUTPUT:
[3, 2, 0, 1]

============================>>
#alternative inc and dec of numbers in list
l=[2,3,1,5,4]
status=True
for i in range(len(l)-1):
    if l[i]<l[i+1] and i%2==0:
        status=True
    elif l[i]>l[i+1] and i%2==1:
        status=True
    else:
        status=False
        break
print(status)

OUTPUT:
True
    
=================================>>

#displaying num acc to +4 index value
n=[2,3,4,1,6,7,8,0]
m=len(n)//2
l=[]
for i in range(m):
    l.extend([n[i],n[i+m]])
print(l)

#OUTPUT:
[2, 6, 3, 7, 4, 8, 1, 0]

==============================>>

a=[1,2,3,1,1,3]
c=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==a[j]:
            c+=1
print(c)
output:
14







