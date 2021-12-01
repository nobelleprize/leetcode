# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

def countSquares(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    result += 1
                else:
                    val = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + matrix[i][j]
                    result += val
                    matrix[i][j] = val
    return result



print(countSquares([[0,1,1,1],
                    [1,1,1,1],
                    [0,1,1,1]]))

print(countSquares([[0,0,1,1],
                    [0,1,1,1],
                    [1,1,1,0],
                    [1,1,1,0],
                    [1,1,1,0]]))
