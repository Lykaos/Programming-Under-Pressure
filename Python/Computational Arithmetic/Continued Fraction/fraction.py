############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#              Hw 3 - Continued Fraction                   #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from fractions import Fraction

def ftd(r):
    result = Fraction(r[len(r) - 1])
    for i in range(len(r) - 2, -1, -1):
        result = 1 / result
        result += int(r[i])
    return result

def dtf(r):
    result = ''
    while r > 0:
        result += str(int(r)) + ' '
        r -= int(r)
        if r > 0:
            r = 1 / r
    return result

sys.stdin.readline()
r1 = sys.stdin.readline().split()
r2 = sys.stdin.readline().split()

dec_r1 = ftd(r1)
dec_r2 = ftd(r2)

print dtf(dec_r1 + dec_r2)
print dtf(dec_r1 - dec_r2)
print dtf(dec_r1 * dec_r2)
print dtf(dec_r1 / dec_r2)