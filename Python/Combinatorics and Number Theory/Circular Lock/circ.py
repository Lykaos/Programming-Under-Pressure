############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                Hw 8 - Circular Lock                      #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from fractions import gcd

for i in range(int(sys.stdin.readline())):
    r1 = map(int, sys.stdin.readline().split())
    r2 = map(int, sys.stdin.readline().split())
    print "Yes" if ((r1[0] + r2[1]) - (r1[1] + r2[0])) % gcd(r1[2], gcd(r1[3], gcd(r2[2], r2[3]))) == 0 else "No"