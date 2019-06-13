############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#          Lab 1 - Problem 1.5: Prefix sums                #
#          Eduardo Rodes Pastor (9406031931)               #
#             Florian Cassayre (980703T092)                #
#                                                          #
############################################################

import sys

class Fenwick:

    def __init__(self, size):
        self.size = size
        self.data = dict.fromkeys(range(1, size+1),0)

    # Adds a number to a certain position in the list
    def add(self, array_position, number_to_add):
        limit = self.size + 1
        while array_position < limit:
            self.data[array_position] += number_to_add
            # Update all the next values for the sum operation, i.e.: right branches of the Binary Indexed Tree
            array_position += (array_position & (-array_position))

    # Sums all the numbers in the array before the given position
    def sum(self, array_position):
        result = 0
        while array_position > 0:
            result += self.data[array_position]
            # Add all the previous values until the next power of 2 (included), i.e.: right branches of the Binary Indexed Tree
            array_position -= (array_position & (-array_position))
        return result