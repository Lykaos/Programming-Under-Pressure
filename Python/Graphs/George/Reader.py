############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#            Lab 2 - Non Negative Weights                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
from Dijkstra import dijkstra 
from Graph import Graph

first_line = sys.stdin.readline().split()

n_intersections = int(first_line[0])
n_streets = int(first_line[1])

second_line = sys.stdin.readline().split()
origin = int(second_line[0])
dest = int(second_line[1])
time_diff = int(second_line[2])
n_intersections_george = int(second_line[3])

v_george = sys.stdin.readline().split()
edges = {}
neighbors = {}

for i in range(n_streets):
    street = sys.stdin.readline().split()
    start = int(street[0])
    end = int(street[1])
    weight = int(street[2])
    edges[start, end] = [weight, sys.maxint]
    edges[end, start] = [weight, sys.maxint]
    if neighbors.get(start) is None:
        neighbors[start] = [end]
    else:
        neighbors[start].append(end)
    if neighbors.get(end) is None:
        neighbors[end] = [start]
    else:
        neighbors[end].append(start)

counter = 0
for i in xrange(1, len(v_george)):
    edges[(int(v_george[i])), int(v_george[i-1])][1] = counter
    edges[(int(v_george[i-1]), int(v_george[i]))][1] = counter
    counter += edges[(int(v_george[i]), int(v_george[i-1]))][0]

parents, distances = dijkstra(Graph(n_intersections + 1, edges, neighbors, origin), time_diff)
print distances[dest]
'''
for i in range(int(first_line[2])):
    d_node = int(sys.stdin.readline())
    print distances[d_node] if distances.get(d_node) is not None else 'Impossible'
    #print getPath(d_node)
print ''
'''
