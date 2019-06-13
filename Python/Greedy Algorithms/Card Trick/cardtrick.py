############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                   Hw 1 - Card trick                      #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def skipPos(pos, i, deck):
    while i >= 0:    
        pos += 1
        if (deck[pos % len(deck)] == 0):
            i -= 1
    return pos

def calculate(num):
    pos = -1
    deck = [0] * num
    for i in range(1, num + 1):
        pos = skipPos(pos, i, deck)
        deck[pos % len(deck)] = i
    return deck
    
# Reader
next(sys.stdin) 
for line in sys.stdin:
    deck = calculate(int(line))
    for item in deck:
        print(item, end='')
        print(' ', end='')
    print()
    
