#WAP to find greatest of four numbers entered by the user

n1 = int(input("Enter the number 1 : "))
n2 = int(input("Enter the number 2 : "))
n3 = int(input("Enter the number 3 : "))
n4 = int(input("Enter the number 4 : "))

if(n1>n2):
    a = n1
else:
    a = n2

if(n3>n4):
    b = n3
else:
    b = n4

if(a>b):
    print(str(a) ,"is the greatest of all ")
else:
    print(str(b),"is the greatest of all")
