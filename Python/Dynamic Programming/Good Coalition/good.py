############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#               Hw 12 - Good Coalition                     #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def solve():
    table = [[0 for i in range(150)] for j in range(len(parties))]
    for i in range(parties[0][0]):
        table[0][i] = float(parties[0][1]) / 100
    for i in range(1, len(parties)):
        seats = parties[i][0]
        prob = float(parties[i][1]) / 100
        for j in range(150):
            if (seats > j):
                if (prob > table[i-1][j]):
                    table[i][j] = prob
                else:
                    table[i][j] = table[i-1][j]
            else:
                if (table[i-1][j-seats] * prob > table[i-1][j]):
                    table[i][j] = table[i-1][j-seats] * prob  
                else:
                    table[i][j] = table[i-1][j]
    maximum = 0
    for i in range(75, 150):
        if table[len(parties) - 1][i] > maximum:
            maximum = table[len(parties) - 1][i]
    return maximum * 100

for i in range(int(sys.stdin.readline())):
    parties = []
    for j in range(int(sys.stdin.readline())):
        parties.append(map(int, sys.stdin.readline().split()))
    print solve()