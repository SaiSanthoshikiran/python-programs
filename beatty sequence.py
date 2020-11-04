#"a number is multiplied by sqrt(2)"
import math
def beatty(n):
    for i in range(1,n+1):
        a=int(i*(2**0.5))
        #for above line we can write as below one
        #a=math.floor(i*math.sqrt(2))
        print(a)
n=int(input("n="))
beatty(n)
