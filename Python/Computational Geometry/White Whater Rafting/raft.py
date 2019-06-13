############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#             Hw 11 - White Water Rafting                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
import math

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def dotProduct(p, s1, s2):
    return (p[0] - s1[0])*(s2[0] - s1[0]) + (p[1] - s1[1])*(s2[1] - s1[1])

def dist_point_to_seg(p, s1, s2):
    a = dist(p, s1)
    b = dist(p, s2)
    c = dist(s1, s2)
    dot = dotProduct(p, s1, s2)

    if dot > 0 and dot < (c ** 2):
        s = (a + b + c) / 2.0
        return 2*math.sqrt(s*(s-a)*(s-b)*(s-c)) / c
    else: 
        return min(a, b)

def solve():
    min_dist = sys.maxint
    for vertex in inner:
        for i in range(len(outer) - 1):
            dist = dist_point_to_seg(vertex, outer[i], outer[i+1])
            if dist < min_dist:
                min_dist = dist
    return min_dist / 2

for i in range(int(sys.stdin.readline())):
    inner = []
    outer = []
    for j in range(int(sys.stdin.readline())):
        inner.append(map(int, sys.stdin.readline().split()))
    for k in range(int(sys.stdin.readline())):
        outer.append(map(int, sys.stdin.readline().split()))
    outer.append(outer[0]) # Last edge
    print solve()