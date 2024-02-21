#WAP to find the sum of first n natural numbers using while loop

n = int(input("Enter the number"))
a = 0
i = 0
while i<=n:
    a = a+i
    i = i+1

print(a)