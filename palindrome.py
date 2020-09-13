#"which appears same both from (left to right) & (right to left)"
n=input("enter the data")
m=n[::-1]
if m==n:
    print(n,'is a palindrome')
else:
    print(n,'is not palindrome')

