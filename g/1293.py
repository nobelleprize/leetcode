from collections import deque

def shortestPath(grid, k):
    directions = [(1,0), (-1,0), (0,1), (0, -1)]
    finish = (len(grid) - 1, len(grid[0]) - 1)

    if k >= len(grid) + len(grid[0]) - 2:
        return len(grid) + len(grid[0]) - 2
        
    queue = deque([(0, (0, 0, k))])
    seen = set()
    seen.add((0,0,k))
    
    while queue:
        steps, (row, col, k) = queue.popleft()

        if (row, col) == finish:
            return steps

        for x, y in directions:
            new_row = row + x
            new_col = col + y

            # if we are within bounds
            if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])):
                new_k = k - grid[new_row][new_col]
                new_state = (new_row, new_col, new_k)

                if new_k >= 0 and new_state not in seen:
                    seen.add((new_row, new_col, new_k))
                    queue.append((steps + 1, (new_row, new_col, new_k)))
        

    return -1

print(shortestPath([
                    [0,0,0],
                    [1,1,0],
                    [0,0,0],
                    [0,1,1],
                    [0,0,0]], 1))
