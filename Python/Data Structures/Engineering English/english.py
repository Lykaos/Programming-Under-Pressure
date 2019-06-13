############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#             Hw 2 - Engineering English                   #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys 

set_words = set()
for line in sys.stdin:
    for word in line.split():
        lower = word.lower()
        if (lower in set_words):
            print '.',
        else:
            set_words.add(lower)
            print word,
    print ''