#WAP to find whether a number is prime or not

num = int(input("Enter the number"))

prime = True

for i in range(2,num):
    if (num%i==0):
        prime = False

if prime:
    print("it's a prime number")
else:
    print("it's not a prime number")