############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                 Hw 12 - Criss Cross                      #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from itertools import combinations
import math

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def overlaps(start, end, middle):
    return dist(start, end) == dist(start, middle) + dist(middle, end)

def isCCW(p1, p2, p3):
    return (p3[1]-p1[1]) * (p2[0]-p1[0]) > (p2[1]-p1[1]) * (p3[0]-p1[0])

def intersect(s1s, s1e, s2s, s2e):
    return isCCW(s1s, s2s, s2e) != isCCW(s1e, s2s, s2e) and isCCW(s1s, s1e, s2s) != isCCW(s1s, s1e, s2e)

def check(c):
    s1s = [c[0][0], c[0][1]]
    s1e = [c[0][2], c[0][3]]
    s2s = [c[1][0], c[1][1]]
    s2e = [c[1][2], c[1][3]]
    if (overlaps(s1s, s1e, s2s) or overlaps(s1s, s1e, s2e)) and (overlaps(s2s, s2e, s1s) or overlaps(s2s, s2e, s1e)):
        return -1
    return intersect(s1s, s1e, s2s, s2e)

def solve(lines):
    cnt = 0
    comb = list(combinations(lines, 2))
    for c in comb:
        if check(c) == -1:
            return -1
        elif check(c):
            cnt += 1
    return cnt

k = int(sys.stdin.readline())
lines = []
for i in range(k):
    lines.append(map(int, sys.stdin.readline().split()))
print solve(lines)