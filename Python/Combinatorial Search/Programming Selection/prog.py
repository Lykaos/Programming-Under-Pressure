############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#            Hw 9 - Programming Selection                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from itertools import combinations

def solve(grouped):
    if len(dic) == len(grouped):
        return "possible"
    mini = 15
    min_idx = -1
    for key in dic.keys():
        if key in grouped:
            continue
        cnt = 0
        for value in dic[key]:
            if value not in grouped:
                cnt += 1
        if cnt < 2:
            return "impossible"
        else:
            if (cnt < mini):
                mini = cnt
                min_idx = key
    ways = combinations(dic[min_idx], 2)
    for w in ways:
        if w[0] in grouped or w[1] in grouped or w[0] not in dic[w[1]]:
            continue
        new_grouped = set(grouped)
        for j in [min_idx, w[0], w[1]]:
            new_grouped.add(j)
        if solve(new_grouped) == "possible":
            return "possible"
    return "impossible"

while (True):
    dic = dict()
    n = int(sys.stdin.readline())
    if (n == 0):
        break
    for i in range(n):
        line = sys.stdin.readline().split()
        for name in line:
            if name not in dic:
                dic[name] = [] 
        dic[line[0]].append(line[1])
        dic[line[1]].append(line[0])
    if (len(dic) % 3 != 0):
        print "impossible" 
    else:
        print solve(set())