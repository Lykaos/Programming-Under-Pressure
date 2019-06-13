############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                    Hw 12 - SETI                          #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from string import ascii_lowercase
import copy

def brute(k, a, r, p):
    x = 0
    while ((k*x + a) % p) != r:
        x += 1
    return x

def solveSystem(eq, p):
    sol = [0 for i in range(len(eq))]
    for i in range(len(eq) - 1, -1, -1):
        a = 0
        for j in range(i+1, len(eq)):
            a += eq[i][j] * sol[j]
        sol[i] = brute(eq[i][i], a, eq[i][len(eq)], p)
    return sol

def reduceSystem(eq, p):
    for i in range(0, len(eq)-1):
        for k in range(i+1, len(eq)):
            f = copy.deepcopy(eq[k][i])
            for j in range(len(eq)+1):
                eq[k][j] -= eq[i][j] * (f / eq[i][i])
                if j == len(eq):
                    eq[k][j] %= p

def generateSystem(n, message):
    k = 1
    eq = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(k ** j)
        row.append(letters[message[i]])
        eq.append(row)
        k += 1
    return eq

def solve(p, message):
    eq = generateSystem(len(message), message)
    reduceSystem(eq, p)
    return solveSystem(eq, p)

letters = {ascii_lowercase[key-1]: key for key in range(1, 27)}
letters['*'] = 0
for i in range(int(sys.stdin.readline())):
    data = sys.stdin.readline().split()
    for i in solve(int(data[0]), data[1]):
        print i,
    print ''