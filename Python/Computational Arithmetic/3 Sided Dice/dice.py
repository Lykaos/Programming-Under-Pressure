############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                 Hw 3 - 3 Sided Dice                      #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def cross_product(p1, p2, p3): # cross product of (p2-p1) and (p3-p1)
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def in_segment(p1, p2, p3): # p3 between p1 and p2
    if ((p1[0] == p3[0] and p1[1] == p3[1]) or (p2[0] == p3[0] and p2[1] == p3[1])):
        return False
    if cross_product(p1, p2, p3) != 0:
        return False
    dot_product = (p3[0] - p1[0]) * (p2[0] - p1[0]) + (p3[1] - p1[1]) * (p2[1] - p1[1])
    if dot_product < 0:
        return False
    sq_length = pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2)
    if dot_product > sq_length:
        return False
    return True

while (True):
    d1 = [int(i) for i in sys.stdin.readline().split()]
    if (d1[0] == 0 and d1[1] == 0 and d1[2] == 0): break
    d2 = [int(i) for i in sys.stdin.readline().split()]
    d3 = [int(i) for i in sys.stdin.readline().split()]
    dx = [int(i) for i in sys.stdin.readline().split()]

    is_segment = (cross_product(d3, d2, d1) == 0)
    if (is_segment):
        print "YES" if (in_segment(d1, d2, dx) or in_segment(d2, d3, dx) or in_segment(d1, d3, dx)) else "NO"
    else:
        same_side_1 = cross_product(d2, d1, dx)
        same_side_2 = cross_product(d3, d2, dx)
        same_side_3 = cross_product(d1, d3, dx)
        print "YES" if (same_side_1*same_side_2 > 0 and same_side_1*same_side_3 > 0) else "NO"
    sys.stdin.readline()