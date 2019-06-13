############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#              Hw 7 - Dictionary Attack                    #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys, random
from string import ascii_letters

def to_letters(s1, s2, digit_pos, n_digits):
    ls1 = list(s1)
    ls2 = list(s2)
    if n_digits == 3:
        for digit in digit_pos:
            ls1[digit] = s2[digit]
    else:
        aux = []
        for i in range(len(s1)):
            if s2[i] not in ls1:
                aux.append(s2[i])
            else:
                ls1[ls1.index(s2[i])] = '_'
        if len(aux) > n_digits:
            return None

        missing_letters = []
        ls1 = list(s1)
        for i in ls2:
            if i in aux:
                missing_letters.append(i)
                aux.remove(i)        
        for i in range(n_digits):
            ls1[digit_pos[i]] = missing_letters[i]
    return ''.join(ls1)

def edit_distance(s1, s2):
    digit_pos = []
    for i in range(len(s1)):
        if s1[i].isdigit():
            digit_pos.append(i)
    n_digits = len(digit_pos)
    if n_digits > 3:
        return None
    if n_digits > 0:
        s1 = to_letters(s1, s2, digit_pos, n_digits)
        if s1 is None:
            return None

    Q = dict()
    for i in range(len(s1)):
        if Q.get(s2[i]) is None:
            Q[s2[i]] = [i]
        else:
            Q[s2[i]].append(i)

    temp = dict.fromkeys(list(ascii_letters), 0)

    P = [0] * (len(s1) + 1)
    for i in range(len(s1)):
        if (Q.get(s1[i])) is None:
            return None
        else:
            try:
                P[i + 1] = 1 + Q[s1[i]][temp[s1[i]]]
                temp[s1[i]] += 1
            except:
                return None
    return (P, n_digits)

def getInvCount(arr):  
    counter = 0
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): counter += 1
    return counter 

dic = set()
for i in range(int(sys.stdin.readline())):
    dic.add(sys.stdin.readline()[:-1])

while True:
    password = sys.stdin.readline()[:-1]
    if password == '': 
        break
    isSafe = True
    for word in dic:
        if len(word) != len(password): 
            continue
        data = edit_distance(password, word)
        if data is None: 
            continue
        if getInvCount(data[0]) + data[1] <= 3:
            isSafe = False
            break
    if isSafe:
        print password

'''
def randomString(stringLength=10):
    return ''.join(random.choice(ascii_letters) for i in range(stringLength))
'''