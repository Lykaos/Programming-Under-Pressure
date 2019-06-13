############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#            Lab 2 - Non Negative Weights                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import heapq
import sys
from Status import Status

def dijkstra(graph, time_diff):
    ''' 
    Calculates the shortest path from a starting node to any other node in a given graph 
    using the Dijkstra algorithm and taking into account time tables.
    :param int graph.n_vertices: The number of nodes in the graph
    :param dict graph.edges: A dictionary with the form {(edge_start, edge_end): edge_weight}
    :param dict graph.neighbors: A dictionary with the form {node: [adjacent_nodes]}
    :param int graph.origin: The starting node in the graph
    '''
    if (graph.neighbors.get(graph.origin) is None):
        return [graph.origin], {graph.origin: 0}
    status = Status(graph)
    computeOriginNode(graph, status, time_diff)
    while status.priority_queue:
        computeNextNode(graph, status, time_diff) 
    return status.parents, status.weights

def computeOriginNode(graph, status, time_diff):
    '''
    Applies Dijkstra to the starting node and adds it to the visited set, taking into account the
    time tables of the adjacent edges.
    :param dict graph.edges: A dictionary with the form {(edge_start, edge_end): [[edge_weight, t0, p], ...]}
    :param dict graph.neighbors: A dictionary with the form {node: [adjacent_nodes]}
    :param int graph.origin: The starting node in the graph
    :param dict status.weights: A dictionary with the form {node: current distance to starting node}
    :param list status.parents: A list of size n_vertices with the current parent (or -1) for every node
    :param set status.visited: A set with all the visited nodes in the graph by the Dijkstra algorithm
    :param list status.priority_queue: A list with all the currently unvisited nodes, being the first one
    the most optimal node to explore next
    '''
    for neighbor in graph.neighbors[graph.origin]:
        edge = graph.edges[(graph.origin, neighbor)]
        minimum_weight = sys.maxint
        if (edge[1] == time_diff):
            next_available_time = 2*edge[0]
        else:
            next_available_time = edge[0]
        if next_available_time < minimum_weight:
            minimum_weight = next_available_time   
        updateStatus(status, neighbor, minimum_weight, graph.origin)
    status.visited.add(graph.origin)

def computeNextNode(graph, status, time_diff):
    '''
    Applies Dijkstra to every reachable node but the starting one and adds them to the visited set, 
    taking into account the time tables of the adjacent edges.
    :param dict graph.edges: A dictionary with the form {(edge_start, edge_end): [[edge_weight, t0, p], ...]}
    :param dict graph.neighbors: A dictionary with the form {node: [adjacent_nodes]}
    :param dict status.weights: A dictionary with the form {node: current distance to starting node}
    :param list status.parents: A list of size n_vertices with the current parent (or -1) for every node
    :param set status.visited: A set with all the visited nodes in the graph by the Dijkstra algorithm
    :param list status.priority_queue: A list with all the currently unvisited nodes, being the first one
    the most optimal node to explore next
    '''
    vertex = heapq.heappop(status.priority_queue)[1]
    if vertex not in status.visited and graph.neighbors.get(vertex) is not None:
        for neighbor in graph.neighbors.get(vertex):
            edge = graph.edges[(vertex, neighbor)]
            minimum_weight = sys.maxint
            if (status.weights[vertex] + time_diff > edge[1] and status.weights[vertex] + time_diff < edge[1] + edge[0]):
                next_available_time = edge[1] + edge[0] + edge[0] - time_diff
            else:
                next_available_time = status.weights[vertex] + edge[0]
            if next_available_time < minimum_weight:
                minimum_weight = next_available_time  
            if status.weights.get(neighbor) is None or status.weights[neighbor] > minimum_weight:
                updateStatus(status, neighbor, minimum_weight, vertex)
    status.visited.add(vertex)

def updateStatus(status, neighbor, new_weight, new_parent):
    '''
    Updates the Dijkstra status variables after exploring a node.
    :param dict status.weights: A dictionary with the form {node: current distance to starting node}
    :param list status.parents: A list of size n_vertices with the current parent (or -1) for every node
    :param list status.priority_queue: A list with all the currently unvisited nodes, being the first one
    the most optimal node to explore next
    :param int neighbor: The current node that we just explored
    :param int new_weight: The new best distance from the starting node to the current node
    :param int new_parent: The new best node we can access the current node from
    '''
    status.weights[neighbor] = new_weight
    status.parents[neighbor] = new_parent
    heapq.heappush(status.priority_queue, [status.weights[neighbor], neighbor])