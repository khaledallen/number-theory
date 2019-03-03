import queue
import math
import sys

def get_gcd_pair(a,b):
    q = queue.Queue()
    pairs = {}

    q.put(a)
    q.put(b)
    pairs[a] = (1,0)
    pairs[b] = (0,1)

    while not q.empty():
        a = q.get()
        b = q.get()
        k = int(math.floor(a/b))
        r = a-k*b

        pairs[r] = (
            pairs[a][0] - k * pairs[b][0],
            pairs[a][1] - k * pairs[b][1]
            )

        print('------------------------------')
        print('{:<10}{:<10}{:<10}'.format(str(pairs[a]),str(pairs[b]),str(pairs[r])))
        print('{:<7} = {:<} * {:<7} + {:>}'.format(a,k,b,r))

        if r != 0:
            q.put(b)
            q.put(r)

    return pairs[b]

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
gcd_pair = get_gcd_pair(a,b)

x = gcd_pair[0]
y = gcd_pair[1]

gcd = a * x + b * y

f = int(c / gcd)
solution = (f * x, f * y) 
print('GCD(' + str(a) + ', ' + str(b) + '): ' + str(gcd))
print('One solution is:')
print('x = ' + str(solution[0]) + ', y = ' + str(solution[1]))
print('For a = ' + str(a) + ' and b = ' + str(b))
print('ax + by = ' + str(a * solution[0] + b * solution[1]))
