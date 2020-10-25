"octal-->>decimal"
##n=int(input('n:'))
##decimal=0
##b=1
##while n:
##    r=n%10
##    n=n//10
##    decimal+=r*b
##    b*=8
##print(decimal)

#----------------------->>

#O -->> D
n=int(input('n'))
c=0
for i in range (0,len(str(n))):
    rem=n%10
    c+=(rem*8**i)
    n=n//10
print(c)
------------------>>

#Decimal ---->> Octal

n=int(input('n:'))
b=''
while n:
    b+=str(n%8)
    n=n//8
print(b[::-1])






















