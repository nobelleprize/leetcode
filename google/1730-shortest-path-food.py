# https://leetcode.com/problems/shortest-path-to-get-food/
from collections import deque

def getFood(grid):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "*":
                start = (row, col, 0)

    queue = deque([(start)])

    while queue:
        r, c, steps = queue.popleft()
        
        for x, y in directions:
            new_r = r + x
            new_c = c + y

            if (0 <= new_r < len(grid)) and (0 <= new_c < len(grid[0])) \
                and grid[new_r][new_c] in ['O','#']:
                
                if grid[new_r][new_c] == "#":
                    return steps + 1

                grid[new_r][new_c] = '|'
                queue.append((new_r, new_c, steps + 1))
    
    return -1

print(getFood([
                ["X","X","X","X","X","X"],
                ["X","*","O","O","O","X"],
                ["X","O","O","#","O","X"],
                ["X","X","X","X","X","X"]]))

print(getFood([
                ["X","X","X","X","X","X","X","X"],
                ["X","*","O","X","O","#","O","X"],
                ["X","O","O","X","O","O","X","X"],
                ["X","O","O","O","O","#","O","X"],
                ["X","X","X","X","X","X","X","X"]]))