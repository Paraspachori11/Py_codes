#write a python function to print first n lines of the following pattern
# ***
# **
# *

n = int(input("enter number \n"))

def star(n):
    for i in range(n):
        a = "*"*(n-i)
        print(a)## if yahan return (a) use karta toh process ek baar execute hoke ruk jaati ,does'nt matter range in that case

print(star(n))