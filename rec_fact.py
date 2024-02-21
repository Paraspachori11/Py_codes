from math import factorial


def fact_iterat(n):
    product = 1
    for i in range(n):  
        product = product*(i+1)
    return product

print(fact_iterat(5))

def fact_recursi(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial=n*fact_recursi(n-1)
        return factorial

print(fact_recursi(9))