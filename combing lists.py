##a=[1,2,3,4]
##b=[2,5,6]
##for i in b:
##    if i in a:
##        pass
##    else:
##        a.append(i)
##print(a)

##------------------>>

a=[1,2,3,4]
b=[2,5,6]
for i in b:
    if i not in a:
        a.append(i)
    
print(a)    
