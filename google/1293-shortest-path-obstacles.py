# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
from collections import deque

def shortestPath(grid, k):
    rows = len(grid)
    cols = len(grid[0])
    target = (rows - 1, cols - 1)

    # if we have sufficient quotas to eliminate the obstacles in the worst case,
    # then the shortest distance is the Manhattan distance
    if k >= rows + cols - 2:
        return rows + cols - 2

    # (row, col, remaining quota to eliminate obstacles)
    origin = (0, 0, k)
    # (steps, state)
    queue = deque([(0, origin)])
    seen = set([origin])

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        steps, (row, col, k) = queue.popleft()

        # we reach the target here
        if (row, col) == target:
            return steps

        # explore the four directions in the next step
        for inc_row, inc_col in dirs:
            new_row = inc_row + row
            new_col = inc_col + col
    
            # if (new_row, new_col) is within the grid boundaries
            if (0 <= new_row < rows) and (0 <= new_col < cols):
                new_k = k - grid[new_row][new_col]
                new_state = (new_row, new_col, new_k)

                # add the next move in the queue if it qualifies
                if new_k >= 0 and new_state not in seen:
                    seen.add(new_state)
                    queue.append((steps + 1, new_state))

    # did not reach the target
    return -1


print(shortestPath([[0,0,0],
                    [1,1,0],
                    [0,0,0],
                    [0,1,1],
                    [0,0,0]], 1))

print(shortestPath([[0,1,1],
                    [1,1,1],
                    [1,0,0]], 1))