############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                Hw 3 - Rational Ratio                     #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from fractions import Fraction
from decimal import Decimal

line = sys.stdin.readline().split()
n = line[0]
n_decimals = len(n[n.find('.'):]) - 1

pow_1 = pow(10, n_decimals - int(line[1]))
pow_2 = pow(10, n_decimals)
n = Decimal(n)

num = int(n * pow_2) - int(n * pow_1)
den = int(pow_2 - pow_1)

sys.stdout.write(str(Fraction(num, den)))

if (num % den == 0):
    print '/1'