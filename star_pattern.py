#WAP to program to print the following star pattern 
#      *          *
#     ***         **
#    *****        ***

from sre_constants import RANGE


n = 4

for i in range(n):
    print("*"*(i+1))

    #another
n=3
for i in range(3):
    print(" " * (n-i-1), end="")
    print ("*" * (2*i+1), end="")
    print(" "* (n-i-1))

