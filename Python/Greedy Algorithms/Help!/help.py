############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#                   Hw 1 - Help!                           #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
sentences = []

def isWord(word):
    return word[0] != '<'
    
def addWordsToDictionary(s1, s2):
    dic = {}

    for i in range(0, 16):

        if (len(s1) != len(s2)):
            return None

        for j in range(0, len(s1)):
            w1 = s1[j]
            w2 = s2[j]

            # w1 and w2 are both words
            if (isWord(w1) and isWord(w2) and w1 != w2):
                return None

            # w1 is a word, w2 is a placeholder
            elif (isWord(w1) and not isWord(w2)):
                if dic.get(w2) is None: # w2 does not exist
                    dic[w2] = ['-', w1]
                elif dic.get(w2)[1] == '-': # w2 exists, but does not have a meaning in that pattern
                    dic[w2][1] = w1
                elif dic.get(w2)[1] == '.': # w2 has appeared at the same position in both patterns
                    dic[w2] = [w1, w1]
                elif dic.get(w2)[1] != w1: # w2 already exists but has another meaning in that pattern
                    return None
                else: # w2 already exists and has w1 as meaning
                    continue

            # w1 is a placeholder, w2 is a word
            elif (not isWord(w1) and isWord(w2)):
                if dic.get(w1) is None: # w1 does not exist
                    dic[w1] = [w2, '-']
                elif dic.get(w1)[0] == '-': # w1 exists, but does not have a meaning in that pattern
                    dic[w1][0] = w2
                elif dic.get(w1)[0] == '.': # w1 has appeared at the same position in both patterns
                    dic[w1] = [w2, w2]
                elif dic.get(w1)[0] != w2: # w1 already has another meaning in that pattern
                    return None
                else: # w1 already has w2 as meaning
                    continue

            # w1 and w2 are both placeholders
            elif (not isWord(w1) and not isWord(w2)):
                if (w1 == w2): # Both placeholders are the same -> w1
                    if dic.get(w1) is None: # w1 does not exist
                        dic[w1] = ['.', '.']
                    elif dic.get(w1)[0] == '-' and dic.get(w1)[1] != '-': # w1 already exists but does not have a meaning in the first pattern
                        dic[w1][0] = dic[w1][1]
                    elif dic.get(w1)[0] != '-' and dic.get(w1)[1] == '-': # w1 already exists but does not have a meaning in the second pattern
                        dic[w1][1] = dic[w1][0]
                    elif dic.get(w1)[0] == '.' and dic.get(w1)[1] == '.': # w1 already has matched with itself before
                        continue
                    elif dic.get(w1)[0] != dic.get(w1)[1]: # w1 has a different meaning in each pattern
                        return None
                else: # Both placeholders are different
                    if dic.get(w2) is None: # w2 does not exist   
                        if dic.get(w1) is None:
                            continue
                        if dic.get(w1)[0] != '-' and dic.get(w1)[0] != '.':
                            dic[w2] = ['-', dic[w1][0]]
                        else:
                            continue
                    elif dic.get(w1) is None: # w1 does not exist
                        if dic.get(w2)[1] != '-' and dic.get(w2)[1] != '.':
                            dic[w1] = [dic[w2][1], '-']
                        else:
                            continue
                    elif dic.get(w1) == ['.', '.']: # w1 already has matched with itself before
                        if dic.get(w2)[1] != '-' and dic.get(w2)[1] != '.':
                            dic[w1] = [dic[w2][1], dic[w2][1]]
                        else:
                            continue
                    elif dic.get(w2) == ['.', '.']: # w2 already has matched with itself before
                        if dic.get(w1)[0] != '-' and dic.get(w1)[0] != '.':
                            dic[w2] = [dic[w1][0], dic[w1][0]]
                        else:
                            continue
                    elif dic.get(w1)[0] == '-' and dic.get(w2)[1] != '-' and dic.get(w2)[1] != '.':
                        dic[w1][0] = dic[w2][1]

                    elif dic.get(w2)[1] == '-' and dic.get(w1)[0] != '-' and dic.get(w1)[0] != '.':
                        dic[w2][1] = dic[w1][0]

                    elif dic.get(w1)[0] != dic.get(w2)[1]:
                        return None
            #print(dic)
    return dic
                
def writeWord(dic, s1, s2):
    if dic is None:
        print('-')
        return

    for j in range(0, len(s1)):
        w1 = s1[j]
        w2 = s2[j]

        # Either w1 or w2 is a word and we write it
        if isWord(w1):
            print(w1, '', end='')
        elif isWord(w2):
            print(w2, '', end='')

        # w1 and w2 do not exist in the dictionary
        elif dic.get(w1) is None and dic.get(w2) is None:
            print('x ', end='')
        
        # w1 does not exist in the dictionary
        elif dic.get(w1) is None and dic.get(w2) is not None:
            if (dic.get(w2)[1] != '-' and dic.get(w2)[1] != '.'):
                print(dic[w2][1], '', end='')
            else:
                print('x ', end='')
        
        # w2 does not exist in the dictionary
        elif dic.get(w1) is not None and dic.get(w2) is None:
            if (dic.get(w1)[0] != '-' and dic.get(w1)[0] != '.'):
                print(dic[w1][0], '', end='')
            else:
                print('x ', end='')

        # w1 and w2 exist in the dictionary and are equal
        elif w1 == w2: 
            if dic.get(w1)[0] != '-' and dic.get(w1)[0] != '.':
                print(dic[w1][0], '', end='')
            elif dic.get(w1)[1] != '-' and dic.get(w1)[1] != '.':
                print(dic[w1][1], '', end='')
            else:
                print('x ', end='')
        
        # w1 and w2 exist in the dictionary and are different
        else:
            if dic.get(w2)[1] != '-' and dic.get(w2)[1] != '.':
                if (dic.get(w1)[0] == '-'):
                    dic[w1][0] = dic.get(w2)[1]
                elif (dic.get(w1)[0] == '.'):
                    dic[w1] = [dic.get(w2)[1], dic.get(w2)[1]]
                print(dic[w2][1], '', end='')
            elif dic.get(w1)[0] != '-' and dic.get(w1)[0] != '.':
                if (dic.get(w2)[1] == '-'):
                    dic[w2][1] = dic.get(w2)[1]
                elif (dic.get(w2)[1] == '.'):
                    dic[w2] = [dic.get(w1)[0], dic.get(w1)[0]]
                print(dic[w1][0], '', end='') 
            else:
                print('x ', end='')
    print()

def solve(sentences):
    i = 0
    while i < len(sentences):

        s1 = sentences[i]
        s2 = sentences[i+1]
        i += 2
        
        if (len(s1) != len(s2)):
            print('-')
            continue

        dic = addWordsToDictionary(s1, s2)
        writeWord(dic, s1, s2)

# Reader
next(sys.stdin) # We do not need the number of test cases
for line in sys.stdin:
    sentences.append(line.split())
    
solve(sentences)
