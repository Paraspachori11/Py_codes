#write a python function to print multiplication table of a given number
n = int(input("enter the number\n"))

def mul(n):
    for i in range(1,11):
        a = n*i
        print(a)
mul(n)
#z = mul(n)
#print(z) #this will cause none includation at the end of table
