# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from collections import deque

def shortestPathBinaryMatrix(grid):
    if grid[0][0] != 0 or grid[len(grid)-1][len(grid)-1] != 0:
        return -1
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    queue = deque()
    queue.append((0,0, 1))
    grid[0][0] = 1
    seen = set()
    seen.add((0,0))

    while queue:
        row, col, distance = queue.popleft()
        if (row, col) == (len(grid)-1, len(grid)-1):
            return distance

        for x, y in directions:
            new_x = x + row
            new_y = y + col

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid):
                if (new_x, new_y) not in seen and grid[new_x][new_y] == 0:
                    seen.add((new_x,new_y))
                    queue.append((new_x,new_y, distance + 1))
    return -1

print(shortestPathBinaryMatrix([[0,1],[1,0]]))
print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))