#KIRAN
for r in range(7):
    for c in range(31):
        if (r in {0,6}) and (c in {0,4}):#k
            print("*",end="")
        elif (r in {1,5}) and (c in {0,3}):
            print("*",end="")
        elif (r in {2,4}) and (c in {0,2}):
            print("*",end="")
        elif (r==3) and (c in {0,1}):
            print("*",end="")
        elif c==8  or(((r==0 or r==6 ) and c!=8)and c in range (6,11)):#I
            print('*',end="")
        elif c==12 or (c==16 and(r!=0 and r!=3)) or ((r==0 or r==3) and(c>12 and c<16)):#R
            print("*",end="")
        elif ((c==18 or c==22)and r!=0 ) or ((r==0 or r==3) and(c>18 and c<22)) :#A
            print("*",end="")
        elif c==24 or c==30 or ((r in {1})and(c in {25}))or ((r in {2})and(c in {26}))or ((r in {3})and(c in {27}))or ((r in {4})and(c in {28}))or ((r in {5})and(c in {29})):#n
            print('*',end="")
        
        elif(c in{5,11,17,23}):
            print(end=" ")
            
        else:
            print(end=" ")
    print()

    --------------------------------------------->>
    #VINAY
    for r in range(5):
    for c in range(33):
        if ( c==0 or c==4) and (r in {0,1,2}):
            print('*',end="")
        elif (r==3) and (c in {1,3}):
            print('*',end="")
        elif (r==4) and (c==2):
            print('*',end="")
        elif c==9  or(((r==0 or r==4 ) and c!=9)and c in range (7,12)):
            print('*',end="")
        elif c==14 or c==18 or ((r in {1})and(c in {15}))or ((r in {2})and(c in {16}))or ((r in {3})and(c in {17})):
            print('*',end="")
        elif ((c==21 or c==25)and r!=0 ) or ((r==0 or r==2) and(c>21 and c<25)) :
            print("*",end="")
        elif  ((r==0) and(c in {28,32})) or (r==1 and(c in {29,31})) or (c==30 and (r in{2,3,4})):
            print("*",end="")
        else:
            print(end=" ")
    print()
