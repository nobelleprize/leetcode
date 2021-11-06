def matrixElementsSum(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                traverseDown(matrix, i, j)
            result += matrix[i][j]
    return result

def traverseDown(matrix, i, j):
    if i >= len(matrix):
        return
    matrix[i][j] = 0
    traverseDown(matrix, i+1, j)

print(matrixElementsSum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3], [1, 1, 1, 1]]))