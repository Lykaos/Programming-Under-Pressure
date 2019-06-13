############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#            Lab 2 - Non Negative Weights                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

class Graph:

    def __init__(self, n_vertices, edges, neighbors, origin):
        self.n_vertices = n_vertices
        self.edges = edges
        self.neighbors = neighbors
        self.origin = origin