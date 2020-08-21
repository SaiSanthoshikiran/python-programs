n=input("enter the num")
asc=n[0]<=n[1]
des=n[0]>=n[1]
i=1
while (i<(len(n)-1)):
    if asc:
        asc=n[i]<=n[i+1]
    elif des:
        des=n[i]>=n[i+1]
    else:
        break
    i+=1
if des:
    print("descending")
elif asc:
    print("ascending")
else:
    print("no format")
