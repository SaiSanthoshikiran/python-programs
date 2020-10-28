def lucky(arr):
    c={}
    for i in arr:
        c[i]=c.get(i,0)+1
    print(c)
    for i in sorted(set(arr),reverse=True):
        if i==c[i]:
            return i
    return -1
arr=list(map(int,input().split()))
print(lucky(arr))
