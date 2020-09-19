##n=input("Enter the number")
##asc=n[0]<=n[1]
##des=n[0]>=n[1]
##i=1
##while (i<(len(n)-1)):
##    if asc:
##        asc=n[i]<=n[i+1]
##    elif des:
##        des=n[i]>=n[i+1]
##    else:
##        break
##    i+=1
##if des:
##    print("descending")
##elif asc:
##    print("ascending")
##else:
##    print("no format")


#---->>

n=int(input("enter the number"))#5432
ac=0
dc=0
x=10
y=0
count=0
while n:
    r=n%10#2,3,4,5
    n//=10#543,54,5
    count+=1
    if x>r:
        x=r
        dc+=1
    if y<r:
        y=r
        ac+=1
if dc==count:
    print("descending order")
elif ac==count:
    print("ascending order")
else :
    print("no order")
       
