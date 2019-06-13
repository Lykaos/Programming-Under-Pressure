############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                    Hw 8 - Zapis                          #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def getInverse(s0):
    if s0 == '(': return ')'
    if s0 == '[': return ']'
    if s0 == '{': return '}'

def solve(s):
    print s
    count = 0
    if '?' not in s:
        return 1
    s0 = s[0]
    for i in range(len(s)):
        if i % 2 != 1:
            continue
        si = s[i]        

        if s0 == '?' and si == '?':
            for i in range(3):
                count += solve(s[1:i]) * solve(s[i+1:len(s)])
        elif s0 == '?' and (si == ')' or si == ']' or si == '}'):
            count += solve(s[1:i]) * solve(s[i+1:len(s)])
        elif si == '?' and (s0 == '(' or si == '[' or si == '{'):
            count += solve(s[1:i]) * solve(s[i+1:len(s)])
    return count

sys.stdin.readline()
s = []
for i in sys.stdin.readline()[:-1]:
    s.append(i)
print solve(s)