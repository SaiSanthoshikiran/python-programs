#"printing sum of arr by excluding last and first elements "
def exclusive(n):
    return(sum(n[1:-1])/(len(n)-2))
n=list(map(int,input().split()))
print(exclusive(n))

OUTPUT:
1 2 3 4 5
3.0
