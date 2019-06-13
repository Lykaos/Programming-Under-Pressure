############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#            Lab 2 - Non Negative Weights                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import heapq

def dijkstra(n_vertices, prices, neighbors, capacity, origin, dest):
    status = Status(origin, n_vertices)
    updateStatus(status, (origin[0], 1), prices[origin[0]], origin)
    while status.priority_queue:
        vertex = heapq.heappop(status.priority_queue)[1]
        if (vertex == dest): break
        if vertex not in status.visited:
            for neighbor in neighbors[vertex]:
                if neighbor[1] > capacity: continue
                cost = prices[vertex[0]] if vertex[0] == neighbor[0] else 0
                if (neighbor not in status.visited or status.weights[neighbor] > cost + status.weights[vertex]):
                    updateStatus(status, neighbor, cost + status.weights[vertex], vertex)
        status.visited.add(vertex)
    return status.parents, status.weights

def updateStatus(status, neighbor, new_weight, new_parent):
    status.weights[neighbor] = new_weight
    status.parents[neighbor] = new_parent
    heapq.heappush(status.priority_queue, [new_weight, neighbor])


class Status:

    def __init__(self, origin, n_vertices):
        self.weights = {origin: 0}
        self.visited = {origin}
        self.priority_queue = []
        self.parents = {}
        for i in range(n_vertices/101):
            for j in range(101):
                self.parents[(i, j)] = -1