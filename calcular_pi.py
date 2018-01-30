from decimal import *

getcontext().prec = 25

def plouffBig(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k)* ((Decimal(4)/(8*k+1)) - (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5)) - (Decimal(1)/(8*k+6))))
        k += 1
    return pi


print(plouffBig(10))