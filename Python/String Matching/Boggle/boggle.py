############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                    Hw 7 - Boggle                         #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def findWord(word, boggle, neighbors, start, pos):
    available = neighbors[start]
    letter = word[pos]
    for i in available:
        if boggle[i] == letter:
            if (pos == len(word) - 1):
                return True
            next_boggle = boggle[:]
            next_boggle[i] = '_'
            if findWord(word, next_boggle, neighbors, i, pos + 1):
                return True
    return False

def solve(dic, boggle, neighbors, scores):
    points = 0
    max_word = ''
    found = 0
    for word in dic:
        if findWord(word, boggle, neighbors, 16, 0):
            points += scores[len(word)]
            if len(word) > len(max_word) or (len(word) == len(max_word) and word < max_word):
                max_word = word
            found += 1
    print points, max_word, found

neighbors = [[1, 4, 5], [0, 2, 4, 5, 6], [1, 3, 5, 6, 7], [2, 6, 7],
            [0, 1, 5, 8, 9], [0, 1, 2, 4, 6, 8, 9, 10], [1, 2, 3, 5, 7, 9, 10, 11], [2, 3, 6, 10, 11],
            [4, 5, 9, 12, 13], [4, 5, 6, 8, 10, 12, 13, 14], [5, 6, 7, 9, 11, 13, 14, 15], [6, 7, 10, 14, 15],
            [8, 9, 13], [8, 9, 10, 12, 14], [9, 10, 11, 13, 15], [10, 11, 14], 
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
scores = [0, 0, 0, 1, 1, 2, 3, 5, 11]

dic = set()
for i in range(int(sys.stdin.readline())):
    dic.add(sys.stdin.readline()[:-1])

sys.stdin.readline()
n_boggles = int(sys.stdin.readline())
for i in range(n_boggles):
    boggle = []
    for j in range(4):
        row = sys.stdin.readline()
        for k in range(4):
            boggle.append(row[k])
    solve(dic, boggle, neighbors, scores)
    sys.stdin.readline()