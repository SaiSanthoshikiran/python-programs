l = [2, 3, 6, 4, 5] 
s=sorted(l)
ans=""
for i in range(len(l)-1):
    if s[i+1]-s[i]==1:
        ans="consecutive"
    else:
        ans="not consecutive"
print(ans)

OUTPUT:
consecutive
