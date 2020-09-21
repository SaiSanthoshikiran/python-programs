##n=int(input('n:'))
##decimal=0
##b=1
##while n:
##    r=n%10
##    n=n//10
##    decimal+=r*b
##    b*=8
##print(decimal)

#---------->>

#Decimal ---->> Octal

n=int(input('n:'))
b=''
while n:
    b+=str(n%2)
    n=n//2
    
print(b[::-1])
