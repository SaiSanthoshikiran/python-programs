##n=int(input('n:'))
##decimal=0
##b=1
##while n:
##    r=n%10
##    n=n//10
##    decimal+=r*b
##    b*=2
##print(decimal)

##------------>>

n=input('n=')
dec=0
j=0
for i in range(len(n)-1,-1,-1):
    dec+=int(n[i])*(2**j)
    j+=1
print(dec)
