
def sum_digits(n):
    n=l
    s=0
    while n>0:
        rem=n%10
        s+=rem**3
        n//=10
        return s
    if l==s:
        print('it is arm')
    else:
        print('not arm')
l=int(input('number'))
print(sum_digits(l))

