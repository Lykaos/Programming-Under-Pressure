############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#             Hw 2 - Engineering English                   #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from fenwick import Fenwick

T = int(sys.stdin.readline())

for i in range(0, T):
    first_line = sys.stdin.readline().split()
    n = int(first_line[0])
    m = int(first_line[1])
    pos = []
    movies = Fenwick(n + m)
    second_line = sys.stdin.readline().split()

    for j in range(0, n):
        pos.append(j + m)
        movies.add(j + m + 1, 1)
    
    for j in range(m, 0, -1):
        idx = int(second_line[abs(j-m)])
        pos_tree = pos[idx-1]
        print movies.sum(pos_tree),
        movies.add(pos_tree, - 1)
        movies.add(j, 1)
        pos[idx-1] = j - 1
    print ''