p=int(input("enter principle amount"))
t=int(input("t="))
r=int(input("r="))
ans=(p*t*r)/100
print(ans)

#compound intrest
p=int(input("enter principle amount"))
t=int(input("t="))
r=int(input("r="))
n=int(input('n='))
a=(p*(1+r/n))**0.5
print(a)
