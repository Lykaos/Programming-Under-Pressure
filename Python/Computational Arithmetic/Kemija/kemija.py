############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                   Hw 3 - Kemija                          #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def setRingValues(start):
    i = 3 + start
    ring1_sum = 0
    min_num = 0
    while (i % n != start):
        k = i % n
        num = ring2[k - 1] - ring2[k - 2] + ring1[k - 3]
        ring1[k] = num
        ring1_sum += num
        min_num = min(num, min_num)
        i += 3
    return (ring1_sum, min_num)

def addChainOffset(start, min_num):
    offset = 1 - min_num
    ring1[start] += offset
    i = 3 + start
    while (i % n != start):
        k = i % n
        ring1[k] += offset
        i += 3
    return ring1

n = int(sys.stdin.readline())
ring1 = [0] * n
ring2 = [0] * n
ring2_sum = 0

for i in range(0, n):
    term = int(sys.stdin.readline())
    ring2_sum += term
    ring2[i] = term

if (n%3 != 0):
    factor = (ring2_sum/3 - setRingValues(0)[0]) / n
    for i in range(0, n):
        ring1[i] += factor
else:
    addChainOffset(0, setRingValues(0)[1])
    addChainOffset(1, setRingValues(1)[1])
    ring1[2] = ring2[1] - ring1[1] - ring1[0]
    setRingValues(2)

for i in range(0, len(ring1)):
    print ring1[i]