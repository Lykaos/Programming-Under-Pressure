############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#            Lab 2 - Non Negative Weights                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from Dijkstra import dijkstra 
import cProfile

def main():
    n_cities, n_roads = [int(i) for i in sys.stdin.readline().split()]
    prices = [int(i) for i in sys.stdin.readline().split()]
    neighbors = {}

    for i in range(n_cities):
        for j in range(100):
            neighbors[(i, j)] = [(i, j + 1)]
        neighbors[i, 100] = []

    for i in range(n_roads):
        start, end, weight = [int(i) for i in sys.stdin.readline().split()]
        for j in range(weight, 101):
            neighbors[(start, j)].append((end, j - weight))
            neighbors[(end, j)].append((start, j - weight))

    for i in range(int(sys.stdin.readline())):
        capacity, origin, dest = [int(i) for i in sys.stdin.readline().split()]
        parents, distances = dijkstra(n_cities*(capacity+1), prices, neighbors, capacity, (origin, 0), dest)
        print distances[(dest, 0)] if distances.get((dest, 0)) is not None else 'impossible'
        
        '''
        path = []
        d_node = (dest, 0)
        if distances.get(d_node) is not None:
            path.append(d_node)
            while (d_node != (origin, 0)):
                parent = parents[d_node]
                path = [parent] + path
                d_node = parent
        print path
        '''
cProfile.run('main()', sort='cumtime')
#main()