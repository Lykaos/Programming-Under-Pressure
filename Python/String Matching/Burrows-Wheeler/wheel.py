############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#               Hw 7 - Burrows-Wheeler                     #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
while (True):
    m = sys.stdin.readline()[:-1]
    if (m == ""): break
    idx = list(range(len(m)))
    s = sorted(idx, key=lambda x: (m[x:len(m)] + m[0:x]))
    
    for c in s:
        sys.stdout.write(m[c-1])
        #print m[c:len(m)] + m[0:c]
    print ''