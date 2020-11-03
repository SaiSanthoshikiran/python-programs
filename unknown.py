a=[2,1,3,5,4,6,7]
k=2
d={}
w=0
while True:
    if a[0]>a[1]:
        w=a[0]
        a.append(a[1])
        a.pop(1)
    else:
        w=a[1]
        a.append(a[0])
        a.pop(0)
    if w not in d:
        d[w]=1
        if d[w]==k:
            print(d[w],w)
            break
    else:
        d[w]=d[w]+1
        if d[w]==k:
            print(w)
