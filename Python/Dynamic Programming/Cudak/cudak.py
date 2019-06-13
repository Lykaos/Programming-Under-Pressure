############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                    Hw 4 - Cudak                          #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def findInteger(a, b, s):
    if b >= a: 
        x = a + (b - a)/2
        nums = solve(str(x), s) - solve(str(a), s)
        if (nums < 1):
            return findInteger(x, b, s) 
        if (nums == 1):
            if (solve(str(x-1), s) == solve(str(a), s)):
                return x
            else:
                return findInteger(a, x, s)
        if (nums > 1):
            return findInteger(a, x, s)
    return

def comb(d, s): 
    if (d == 0): return (s == 0) 
    if (s == 0): return 1
    if (sums_table[d][s] != -1): return sums_table[d][s]
    result = 0
    for i in range(10): 
        if (s >= i): result += comb(d - 1, s - i) 
    return result

def solve(N, S):
    if (N == '0'): return (S == 0)
    result = 0
    if (len(N) > 0 and S >= 0):
        for i in range(S, S - int(N[0]), -1):
            result += comb(len(N) - 1, i) 
            sums_table[len(N) - 1][i] = comb(len(N) - 1, i)
            if (i == 0): break    
        S -= int(N[0])
        N = N[1:] if len(N) > 1 else '0'
        result += solve(N, S)
    return result

sums_table = [[-1 for i in range(136)] for i in range(16)]
for i in range(16):
    for j in range(136):
        sums_table[i][j] = comb(i, j) 
line = sys.stdin.readline().split()
A = int(line[0])
B = int(line[1])
S = int(line[2])
print solve(str(B), S) - solve(str(A- 1), S)
print findInteger(A, B, S)