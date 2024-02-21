#Write a recursive function to calculate the sum of first n natural numbers

#sum(n) = 1+2+3+4+5+....+(n-1)+n
#i.e sum(n) = sum(n-1)+n

def sum(n):
    if n==1:
        return 1
    else:
        Add = n+sum(n-1)
        return Add

z = sum(5)
print(z)