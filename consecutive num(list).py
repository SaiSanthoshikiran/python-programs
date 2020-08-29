
##error
l = [2, 3, 8, 4, 5] 
s=sorted(l)
cons=s[0]<s[1]

for i in range(len(l)):#
    if cons:
        s[i]-s[i-1]==1
    else:
        s[i]-s[i-1]!=1

if cons:
    print(s,"consecutive")
else:
    print(s,"not consecutive")
