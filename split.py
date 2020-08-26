##n=input('enter the value')
##print(list(n.split(" ")))

#---------------->>
#using function
def split_string(string):
    l=list(string.split(""))
    return l

str=input("enter the input")
print(split_string(str))
