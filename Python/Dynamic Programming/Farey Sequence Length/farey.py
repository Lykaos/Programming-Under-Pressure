############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#            Hw 12 - Farey Sequence Length                 #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from totient import euler_totient

mem = [2 for i in range(10001)]
for i in range(2, 10001):
    mem[i] = mem[i-1] + euler_totient[i]
for i in range(int(sys.stdin.readline())):
    data = map(int, sys.stdin.readline().split())
    print data[0], mem[data[1]]