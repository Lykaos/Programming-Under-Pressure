############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#             Hw 4 - Uxuhul Voting System                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

outcomes = [[2, 3, 5], [1, 4, 6], [1, 4, 7], [2, 3, 8], [1, 6, 7], [2, 5, 8], [3, 5, 8], [4, 6, 7]]
stones = ['NNN', 'NNY', 'NYN', 'NYY', 'YNN', 'YNY', 'YYN', 'YYY']
    
def look_outcomes(priest_pref, possible_outcomes, iv):
    if len(iv) == 0:
        for i in priest_pref:
            if int(i) in possible_outcomes:
                return i
    else:
        next_outcomes = [iv[possible_outcomes[0] - 1], iv[possible_outcomes[1] - 1], iv[possible_outcomes[2] - 1]]
        for i in priest_pref:
            if i in next_outcomes:
                return i
    
def solve():
    iv = []
    for i in range(n_priests - 1, -1, -1):
        priest_votes = []
        for j in range(0, 8):
            priest_votes.append(look_outcomes(preferences[i], outcomes[j], iv))
        iv = priest_votes[:]
        votes.append(priest_votes)
    print stones[int(votes[n_priests - 1][0]) - 1]

n_tests = int(sys.stdin.readline())

for i in range(n_tests):
    n_priests = int(sys.stdin.readline())
    preferences = []
    votes = []
    for j in range(n_priests):
        line = sys.stdin.readline().split()
        pref = [0] * 8
        for k in range(len(line)):
            pref[int(line[k]) - 1] = str(k + 1)
        preferences.append(pref)
    solve()

