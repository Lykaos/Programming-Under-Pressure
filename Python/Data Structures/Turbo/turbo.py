############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#             Hw 2 - Engineering English                   #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from fenwick import Fenwick

n = int(sys.stdin.readline())
lowest = 1
highest = n
tree = Fenwick(n)

position = [0] * (n+1)

for i in range(0, n):
    position[int(sys.stdin.readline())] = i+1
    tree.add(i+1, 1)

for i in range(1, n+1):
    if (i % 2 == 1):
        tree.add(position[lowest], -1)
        print tree.sum(position[lowest])
        lowest += 1
    else:
        tree.add(position[highest], -1)
        print (tree.sum(n) - tree.sum(position[highest]))
        highest -= 1