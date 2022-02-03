# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from itertools import count


def countSquares(matrix):
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                if row == 0 or col == 0:
                    result += matrix[row][col]
                else:
                    neighbors = min(matrix[row-1][col], matrix[row-1][col-1], matrix[row][col-1])
                    if matrix[row][col] > 0 and neighbors > 0:
                        matrix[row][col] = neighbors + 1
                    result += matrix[row][col]
    return result

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
print(countSquares([[1,0,1],[1,1,0],[1,1,0]]))