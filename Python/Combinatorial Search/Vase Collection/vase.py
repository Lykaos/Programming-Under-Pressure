############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#               Hw 9 - Vase Collection                     #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from itertools import combinations

def solve():
    n_items = max(10, len(max(dic.values(), key=lambda x: len(x))))
    while (True):
        if n_items == 1:
            return 1
        comb_set = set()
        for key in dic.keys():
            if len(dic[key]) >= n_items:
                comb_set.add(key)
        for w in combinations(comb_set, n_items):
            inter = dic[w[0]]
            for x in range(1, n_items):
                inter = inter & dic[w[x]]
            if len(inter) == n_items:
                return n_items
        n_items -= 1
    return None

for i in range(int(sys.stdin.readline())):
    dic = dict()
    for i in range(int(sys.stdin.readline())):
        line = map(int, sys.stdin.readline().split())
        if line[0] not in dic:
            dic[line[0]] = set()
        dic[line[0]].add(line[1])
    print solve()