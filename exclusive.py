def exclusive(n):
    return(sum(n[1:-1])//(len(n)-2))
n=list(map(int,input().split()))
print(exclusive(n))
