# https://leetcode.com/problems/maximal-square/

def maximalSquare(matrix):
    if not matrix or len(matrix) < 1:
        return 0

    result = 0
    
    dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == '1':
                dp[row+1][col+1] = min(dp[row][col], dp[row][col+1], dp[row+1][col+1]) + 1
                if dp[row+1][col+1] > result:
                    result = dp[row+1][col+1]
    return result * result

# print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
# print(maximalSquare([['1','1','1','0'], ['1','1','1','0'], ['1','1','1','0'], ['1','1','1','0']]))
print(maximalSquare([["1"]]))