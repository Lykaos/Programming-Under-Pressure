############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#               Hw 8 - Rasterized Lines                    #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from fact import factorize
from itertools import combinations

def totient(n):
    factors = set(factorize(n))
    for f in factors:
        n -= n / f
    return n

def getDivisors(n):
    factors = factorize(n)
    divisors = set([1, n])
    for i in range(1, len(factors)):
        for j in set(combinations(factors, i)):
            divisors.add(reduce(lambda x, y: x*y, j))
    return divisors

def solve(k):
    res = 0
    for d in getDivisors(k):
        res += totient(k/d + 1)
    return res
    
for i in range(int(sys.stdin.readline())):
    print solve(int(sys.stdin.readline()))