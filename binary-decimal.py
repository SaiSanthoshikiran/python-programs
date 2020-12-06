Binary--->> Decimal

##n=int(input('n:'))
##decimal=0
##b=1
##while n:
##    r=n%10
##    n=n//10
##    decimal+=r*b
##    b*=2
##print(decimal)

##------------------>>
B---->>D

n=input('n=')
dec=0
j=0
for i in range(len(n)-1,-1,-1):
    dec+=int(n[i])*(2**j)
    j+=1
print(dec)

#-------------------->>

#Decimal ---->> Binary

n=int(input('n:'))
b=''
while n:
    b+=str(n%2)
    n=n//2
    
print(b[::-1])
