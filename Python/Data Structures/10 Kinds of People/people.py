############################################################
#                                                          #
#  DD2458 Problem Solving and Programming Under Pressure   #
#              Hw 2 - 10 Kinds of People                   #
#          Eduardo Rodes Pastor (9406031931)               #
#                                                          #
############################################################

import sys
import cProfile

def findPath(r1, c1, r2, c2, maze):
    pending = set()
    pending.add((r1, c1))
    visited = set()
    sol = 'decimal' if (maze[r2-1][c2-1] == '1') else 'binary'
    rows = len(maze)
    cols = len(maze[0])
    while len(pending) > 0:
        for square in list(pending):
            sq0 = square[0]
            sq1 = square[1]
            current_square = maze[sq0-1][sq1-1]
            visited.add((sq0, sq1))
            if (sq0 < rows and maze[sq0][sq1-1] == current_square and (sq0 + 1, sq1) not in visited):
                if (sq0+1 == r2 and sq1 == c2):
                    return sol
                pending.add((sq0 + 1, sq1))
            if (sq0 > 1 and maze[sq0-2][sq1-1] == current_square and (sq0 - 1, sq1) not in visited):
                if (sq0-1 == r2 and sq1 == c2):
                    return sol
                pending.add((sq0 - 1, sq1))
            if (sq1 < cols - 1 and maze[sq0-1][sq1] == current_square and (sq0, sq1 + 1) not in visited):    
                if (sq0 == r2 and sq1+1 == c2):
                    return sol     
                pending.add((sq0, sq1 + 1))
            if (sq1 > 1 and maze[sq0-1][sq1-2] == current_square and (sq0, sq1 - 1) not in visited):  
                if (sq0 == r2 and sq1-1 == c2):
                    return sol
                pending.add((sq0, sq1 - 1))
            pending.remove((sq0, sq1))
    return "neither"
        
def solve(r1, c1, r2, c2, maze):
    if (maze[r1-1][c1-1] != maze[r2-1][c2-1]):
        return "neither" 
    return findPath(r1, c1, r2, c2, maze)

maze = []
result = ''

def main(maze, result):
    for i in range(0, int(sys.stdin.readline().split()[0])):
        maze.append(sys.stdin.readline())
    for i in range(0, int(sys.stdin.readline())):
        case = sys.stdin.readline().split()
        result += solve(int(case[0]), int(case[1]), int(case[2]), int(case[3]), maze) + '\n'
    print result[:-1]

cProfile.run('main(maze, result)', sort='tottime')
#main(maze, result)