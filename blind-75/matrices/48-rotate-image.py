def rotate(matrix):
    transpose(matrix)
    # reflect(matrix)
    return matrix

def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] #= matrix[i][j], matrix[j][i]

def reflect(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(rotate([
                [1,  2,  3,  4,  5], 
                [6,  7,  8,  9,  10], 
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]]))