n=str(input('n'))
for i in range(0,len(n)):
    for j in range (0,i+1):
        print(n[j],end="")
    print()
