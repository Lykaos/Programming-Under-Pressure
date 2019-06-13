############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                  Hw 9 - Tautology                        #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def calculate(line):
    if len(line) == 1:
        return int(line[0])
    if line[0] == 'N':
        return not calculate(line[1:len(line)])
    cnt = 0
    for c in range(len(line)):
        if line[c] in ['K', 'A', 'C', 'E']:
            cnt += 1
        if line[c] in ['0', '1']:
            cnt -= 1
            if cnt == 0:
                first = calculate(line[1:c+1])
                second = calculate(line[c+1:len(line)])
                if line[0] == 'K':
                    return first and second
                if line[0] == 'A':
                    return first or second
                if line[0] == 'C':
                    return (not first) or second
                if line[0] == 'E':
                    return first == second
    return None

def solve(line):
    available = []
    for character in line:
        if character in ['p', 'q', 'r', 's', 't'] and character not in available:
            available.append(character)
    for i in range(pow(2, len(available))):
        new_line = line[:]
        binary = list("{:05b}".format(i))[::-1]
        for j in range(len(available)):
            new_line = new_line.replace(available[j], binary[j])
        if calculate(list(new_line)) == 0:
            return "not"
    return "tautology"

while (True):
    line = sys.stdin.readline()[:-1]
    if (line == '0'):
        break
    print solve(line)