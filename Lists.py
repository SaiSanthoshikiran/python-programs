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

===============================>>





