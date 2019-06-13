############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                Hw 10 - Cuckoo Hashing                    #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from copy import deepcopy

def add(line):
    calls = 0
    while (True):
        calls += 1
        if calls == 100:
            return 0
        first = dic[line[0]]
        second = dic[line[1]]
        if first == 0:
            dic[line[0]] = line
            return 1
        elif first != 0 and second == 0:
            dic[line[1]] = line
            return 1
        elif first != 0 and second != 0:
            aux = deepcopy(first)
            dic[line[0]] = line
            line = [aux[1], aux[0]]

for i in range(int(sys.stdin.readline())):
    successful = True
    data = map(int, sys.stdin.readline().split())
    dic = dict.fromkeys(range(data[1]), 0) 
    for j in range(data[0]):
        if add(map(int, sys.stdin.readline().split())) == 0:
            successful = False
            for k in range(j+1, data[0]):
                sys.stdin.readline()
            break
    print "successful hashing" if successful else "rehash necessary"