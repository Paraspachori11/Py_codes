#WAP using function to find the greatest of three numbers


a = int(input("enter the first number \n"))
b = int(input("enter the second number \n"))
c= int(input("enter the third number \n"))

def greatest(a,b,c):
    if (a>b):
        if (a>c):
            return a
        else:
            return c
    if (b>c):
        return b
    else :
        return c

print(greatest(a,b,c))




