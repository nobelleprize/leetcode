# https://leetcode.com/problems/number-of-islands/

def numIslands(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                counter += 1
                islandDFS(grid, i, j)
    return counter


def islandDFS(grid, i, j):
    if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return
    
    grid[i][j] = '0'

    islandDFS(grid, i-1, j)
    islandDFS(grid, i+1, j)
    islandDFS(grid, i, j+1)
    islandDFS(grid, i, j-1)

print(numIslands([["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"], 
["0","0","0","1","1"]
                    ]))


