import math
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def gcd(a,b):
    if b == 0:
        return a

    k = int(math.ceil(a/b))
    l = int(math.floor(a/b))
    c = min(abs(a-k*b),abs(a-l*b),abs(a+k*b),abs(a+l*b))
    # Some bookkeeping for printing which option we used
    if c == abs(a-k*b):
        f = k
        s = '+'
    elif c == abs(a+k*b):
        f = -k
        s = '-'
    elif c == abs(a-l*b):
        f = l
        s = '+'
    elif c == abs(a+l*b):
        f = -l
        s = '-'
    print(str(a) + " = " + str(f) + " * " + str(b) + " " + s + " " + str(c))
    return gcd(b, c)

print("The GCD of " + str(a) + " and " + str(b) + ":")
print(gcd(a,b))

