a={1:5,2:4,3:6}
##for i in a.keys():
##    print(i,a[i])
for i,j in a.items():
    print(i,j)
##OUTPUT:
##1 5
##2 4
##3 6

#----------------->>

##for i in a.values():
##    print(i)
##
##OUTPUT:
##5
##4
##6

#----------------->>

##a={}
##n=int(input('no.of students:'))
##for i in range(n):
##    k=input('enter student name:')
##    v=[]
##    p=int(input('enter no.of subjects:'))
##    for j in range(p):
##        s=input('enter subject marks:')
##        v.append(s)
##    a[k]=v
##print(a)
##
##OUTPUT:
##no.of students:2
##enter student name:kiran
##enter no.of subjects:3
##enter subject marks:2
##enter subject marks:3
##enter subject marks:4
##enter student name:Janu
##enter no.of subjects:3
##enter subject marks:3
##enter subject marks:4
##enter subject marks:5
##{'kiran': ['2', '3', '4'], 'pichi': ['3', '4', '5']}

##-------------------------->>

a={}
n=int(input('enter no.of students:'))
for i in range(1,n+1):
    k=input('enter stu. name:')
    a[k]=list(map(int,input('enter marks:').split()))
print(a)

OUTPUT:
enter no.of students:4
enter stu. name:k
enter marks:6 7 8 
enter stu. name:j
enter marks:8 6 9
enter stu. name:l
enter marks:5 6 
enter stu. name:i
enter marks:7 6
{'k': [6, 7, 8], 'j': [8, 6, 9], 'l': [5, 6], 'i': [7, 6]}
























