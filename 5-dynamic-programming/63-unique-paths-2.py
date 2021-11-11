# https://leetcode.com/problems/unique-paths-ii/

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
        return 0

    obstacleGrid[0][0] = 1

    blocked = False

    for i in range(1, m):
        if obstacleGrid[i][0] == 1:
            obstacleGrid[i][0] = '*'
            blocked = True
        elif blocked == False:
            obstacleGrid[i][0] = 1

    blocked = False
        
    for i in range(1, n):
        if obstacleGrid[0][i] == 1:
            obstacleGrid[0][i] = '*'
            blocked = True
        elif blocked == False:
            obstacleGrid[0][i] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1 or obstacleGrid[i][j] == '*':
                obstacleGrid[i][j] = '*'
            else:
                a = obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != '*' else 0
                b = obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != '*' else 0

                obstacleGrid[i][j] = a + b

    return obstacleGrid[m-1][n-1]

print(uniquePathsWithObstacles([[0,1,0],[0,0,0],[0,0,0]]))
print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
# print(uniquePathsWithObstacles([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]]))
