############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#            Lab 2 - Non Negative Weights                  #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

class Status:

    def __init__(self, graph):
        self.weights = {graph.origin: 0}
        self.parents = [-1] * graph.n_vertices
        self.visited = set()
        self.priority_queue = []