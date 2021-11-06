# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix):
    row_set = set()
    col_set = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                row_set.add(row)
                col_set.add(col)
    makeZero(matrix, row_set, col_set)
    return matrix

def makeZero(matrix, row_set, col_set):
    for row in row_set:
         matrix[row][0:] = [0] * len(matrix[0])

    for col in col_set:
        for row in range(len(matrix)):
            matrix[row][col] = 0
# print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
