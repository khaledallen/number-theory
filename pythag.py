import sys

n = int(sys.argv[1])
trips = []

for l in range(1,n):
    for k in range(1,10):
        m = (-l/k)
        a = (-2*m)
        b = (1-(m**2))
        c = (1+m**2)
        tripleStr = "(" + str(a) + "," + str(-b) + "," + str(c) + ")"
        if a**2 + b**2 == c**2 and a != 0 and b != 0 and tripleStr not in trips:
            trips.append(tripleStr)
            print(tripleStr)
            if b%11 == 0: print("11:" + str(m))
