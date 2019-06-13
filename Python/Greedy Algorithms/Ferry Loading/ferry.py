############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#              Hw 1 - Ferry Loading III                    #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def getPos(num):
    return "left" if num == 0 else "right"

def load(cars, capacity, triptime, initial_pos):
    pos = 0
    time = 0
    while (len(cars[0]) > 0 or len(cars[1]) > 0):
        inv_pos = 1 if pos == 0 else 0
        loaded = 0
        both_cars = len(cars[pos]) > 0 and len(cars[inv_pos]) > 0
        if len(cars[pos]) == 0 or (both_cars and cars[pos][0] > cars[inv_pos][0] and cars[pos][0] > time):
            pos = inv_pos
            time = max(time, cars[pos][0]) + triptime
        elif len(cars[inv_pos]) == 0 or (both_cars and cars[pos][0] <= cars[inv_pos][0]):
            time = max(time, cars[pos][0])

        for t in list(cars[pos]):
            if t <= time:
                loaded += 1
                initial_pos[initial_pos.index([str(t), getPos(pos)])] = time + triptime
                cars[pos].pop(0)
            if loaded == capacity or t > time:
                break
        time += triptime
        pos = 1 if pos == 0 else 0
    for i in initial_pos:
        print i
    print ''

for i in range(int(sys.stdin.readline())):
    data = map(int, sys.stdin.readline().split())
    cars = [[], []]
    initial_pos = []
    for i in range(data[2]):
        line = sys.stdin.readline().split()
        initial_pos.append(line)
        if line[1] == 'left':
            cars[0].append(int(line[0]))
        else:
            cars[1].append(int(line[0]))
    load(cars, data[0], data[1], initial_pos)