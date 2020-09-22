#Binary -->> Decimal
n=int(input('h'))
h=''
while n:
    r=n%16
    if r<10:
        h+=str(chr(r+48))
    else:
        h+=str(chr(r+55))
print(h[::-1])
