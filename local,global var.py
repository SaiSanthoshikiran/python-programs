##a=10
##print(a)
##def ex():
##    a=10
##    a+=1
##    print(a)
##ex()
##print(a)


##def sum_digits(l):
##    n=l
##    s=0
##    while l>0:
##        rem=l%10
##        s+=rem**3
##        #l//=10
##        return s
##    if n==s:
##        print('it is arm')
##    else:
##        print('not arm')
##l=int(input('number'))
##print(sum_digits(l))


##
##n=input()
##s=0
##for i in n:
##    s+=int(i)
##print(s)

#---------->>
l=int(input('number'))
n=l
s=0
while l>0:
    rem=l%10
    s+=rem**3
    l//=10
if n==s:
    print('it is arm')
else:
    print('not arm')

