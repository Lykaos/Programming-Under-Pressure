############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#           Hw 4 - Adventures in Moving IV                 #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys

def getNextStations(station, capacity):
    available_stations = []
    while (station + len(available_stations) + 1 < n_stations and distances[station + len(available_stations) + 1] - distances[station] <= capacity):
        available_stations.append(station + len(available_stations) + 1)
    return available_stations

def solve():
    for station in range(n_stations):
        for capacity in range(201):
            for next_station in getNextStations(station, capacity):
                if (cost[station][capacity] < cost[next_station][capacity - (distances[next_station] - distances[station])]):
                    cost[next_station][capacity - (distances[next_station] - distances[station])] = cost[station][capacity]
            for load in range(201 - capacity):
                if (cost[station][capacity] + load*prices[station] < cost[station][load + capacity]):
                    cost[station][load + capacity] = cost[station][capacity] + load*prices[station]
    optimal_cost = cost[n_stations - 1][100]
    print optimal_cost if (optimal_cost != sys.maxint) else "Impossible"

total_dist = int(sys.stdin.readline())
n_stations = 2
cost = [[sys.maxint] * 201]
distances = [0]
prices = [sys.maxint]
for line in sys.stdin:
    spl = line.split()
    distances.append(int(spl[0]))
    prices.append(int(spl[1]))
    cost.append([sys.maxint] * 201)
    n_stations += 1
cost.append([sys.maxint] * 201)
cost[0][100] = 0
distances.append(total_dist)
prices.append(sys.maxint)
solve()