#"which appears same both from (left to right) & (right to left)"
n=input("enter the data")
m=n[::-1]
if m==n:
    print(n,'is a palindrome')
else:
    print(n,'is not palindrome')

======================>>
n=input()
if n==n[::-1]:
    print('palindrome')
else:
    print('not a palindrome')
    
=========================>>
n=input()
m=len(n)
for i in range(0,int(m-1)):
    if n[i]!=n[m-i-1]:
        print('not palindrome')
    else:
        print('palindome')
