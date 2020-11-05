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
??????????
n=input()
for i in range(len(n)/2):
    if a(i)==a(i-1):
        print('')
