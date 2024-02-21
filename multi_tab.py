#WAP to print a multiplication table of a given number

a = int(input("Multiplication table of : \n"))

b = int(input("Till number \n"))

print("Table of "+str(b)+" is :")

for i in range(1,b+1):
    c = a*i
    print(c)


##Alter(using f string)
num = int(input("Enter the number :"))

for i in range(1,11):
    print(f"{num}X{i}={num*i}")


