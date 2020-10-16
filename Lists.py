#"displaying zeroes at last in output"
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
#no.of times values will be equal based on index values
a=[1,2,3,1,1,3]
c=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==a[j]:
            c+=1
print(c)
output:
14

===============================>>
if  each candies value is added to extra candy then value is >= max(candies) i.e 5 then true /else false is printed--------2+3=5>>True,1+3=4>>False
##candies=[2,3,5,1,2] 
###extra_candies=3
##x=3
##l=[]
##for i in candies:
##    if i+x>=max(candies):
##        l.append(True)
##    else:
##        l.append(False)
##print(l)
##             [or]

##a=[2,3,5,1,2]
##x=3
##m=max(a)
##l=[True if i+x>=m else False for i in a]
##print(l)

##OUTPUT:
##[True, True, True, False, True]

=========================================>>
#displaying last and first index value of target number 
n=int(input('n:'))
l=list(map(int,input().strip().split()))[:n]
key=int(input())
L=sorted(l)
arr=[]
c=0
for i in range (len(L)):
    if l[i]==key:
        arr.append(c)
    c+=1
    
if len(arr)!=0:
    print(arr[0],arr[-1])
else:
    print("-1 -1")

OUTPUT:
n:5
1 2 2 3 3
2
1 2

================================>>
after arrange in ascending oredr no.of values changed its index value is displayed

a=[1,1,4,2,1,3]
b=sorted(a)#[1,1,1,2,3,4]
c=0
for i in range(len(a)):
    if a[i]!=b[i]:
        c+=1
print(c)
    
output:
3

================================>>

p=[8,4,6,2,3]
l=[]
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]>p[j]:
            l.append(p[i]-p[j])
            break
        else:
            l.append(p[i])
print(l)

OUTPUT:
[4, 4, 2, 4, 2]

===============================>>

#"checking whether the max val of list is greater than twice of the rem elements"
n=[3,6,1,0]
m=max(n)
b=n.copy()
b.remove(m)
c=0
for i in b:
    if m>=2*i:
        c+=1
if c==len(b):
    print(n.index(m))
else:
    print(-1)

OUTPUT:
1

======================>>

##"check whether the target num is in list or not ,if yes then print its index value or else insert the target element in order and print its index val"
n=[1,3,5,6]
t=4
if t in n:
    print(n.index(t))
else:
    n.append(t)
    n.sort()
    print(n.index(t))

OUTPUT:
2

-------------------->>

heap,num,itr=list(map(int,input().split())),int(input()),0
while heap[itr]<num:
    itr+=1
print(itr)

=================================>>

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

============================>>









