############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#             Hw 11 - White Water Rafting                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from itertools import combinations

def isCCW(p1, p2, p3):
    return (p3[1]-p1[1]) * (p2[0]-p1[0]) > (p2[1]-p1[1]) * (p3[0]-p1[0])

def intersect(s1s, s1e, s2s, s2e):
    return isCCW(s1s, s2s, s2e) != isCCW(s1e, s2s, s2e) and isCCW(s1s, s1e, s2s) != isCCW(s1s, s1e, s2e)

def check(c):
    s1s = [c[0][0], c[0][1]]
    s1e = [c[0][2], c[0][3]]
    s2s = [c[1][0], c[1][1]]
    s2e = [c[1][2], c[1][3]]
    s3s = [c[2][0], c[2][1]]
    s3e = [c[2][2], c[2][3]]
    return intersect(s1s, s1e, s2s, s2e) and intersect(s1s, s1e, s3s, s3e) and intersect(s2s, s2e, s3s, s3e)

def solve(lines):
    cnt = 0
    comb = list(combinations(lines, 3))
    for c in comb:
        if check(c):
            cnt += 1
    return cnt

while (True):
    k = int(sys.stdin.readline())
    if k == 0:
        break
    lines = []
    for i in range(k):
        lines.append(map(float, sys.stdin.readline().split()))
    print solve(lines)