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









