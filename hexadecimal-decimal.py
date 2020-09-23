#Decimal---->>Hexa Decimal
n=int(input('h'))
h=''
while n>0:
     a=n%16
     if a>=10 and a<=15:
         a=a%10
         h+=chr(65+a)
     else:
         h+=str(a)
     n=n//16
print(h[::-1])

------------------------->>
hexa-->>Decimal

n=int(input('n'))
d=0
b=1
for i in ra nge(len()):
    r=n[-1]
    if r.isdigit():
        d+=(ord()-48)*b
    else:
        d+=(ord(r)-55)
    n=n[:-1 ]
