
def minPathSum(grid):
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)-1,-1,-1):
        for col in range(len(grid[0])-1,-1,-1):

            if row == len(grid)-1 and col != len(grid[0])-1: # last row but not last column, look right
                dp[row][col] = grid[row][col] + dp[row][col+1]

            elif col == len(grid[0])-1 and row != len(grid)-1: # last column but not last row, look down
                dp[row][col] = grid[row][col] + dp[row+1][col]

            elif row != len(grid)-1 and col != len(grid[0])-1: # look down and right
                dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])
            
            else:
                dp[row][col] = grid[row][col]
    return dp[0][0]


# print(minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))


# grid = [[1,3,1],[1,5,1],[4,2,1]]
# for i in range(len(grid)-1, -1, -1):
#     for j in range(len(grid[0])-1, -1, -1):
#         print(i, j)


