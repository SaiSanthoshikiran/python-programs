#"printing the num if no.of occurences and the num is same --lucky num ,in case 2 or more possible outcomes printing the largest val"
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

OUTPUT:
1 2 2 3 4 
{1: 1, 2: 2, 3: 1, 4: 1}
2
