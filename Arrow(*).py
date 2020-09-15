###" arrow pattern "
def pattern(n):
    for i in range(n):#2,-2
        for j in range(1,abs(i)+1):
            print(' ',end="")
        for k in range(1,abs(i)+2):
            print('* ',end="")
        print()
n=int(input('n'))
pattern(n)
