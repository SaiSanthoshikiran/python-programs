#Decimal---->>Hexa Decimal
n=int(input('h'))
h=''
while n:
    r=n%16
    if r<10:
        h+=str(chr(r+48))
    else:
        h+=str(chr(r+55))
print(h[::-1])

#hexa-->>Decimal
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
