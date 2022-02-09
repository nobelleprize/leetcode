# https://leetcode.com/problems/spiral-matrix/

def spiralOrder(matrix):
    return spiralOrderUtil(matrix, len(matrix), len(matrix[0]))


def spiralOrderUtil(matrix, end_row, end_col):
    result = []
    start_row = 0
    start_col = 0
    while start_row < end_row and start_col < end_col:

        # left to right
        for i in range(start_col, end_col):
            result.append(matrix[start_row][i])
        start_row += 1
        
        # top to bottom
        for i in range(start_row, end_row):
            result.append(matrix[i][end_col - 1])
        
        end_col -= 1

        # right to left
        if start_row < end_row:
            for i in range(end_col - 1, (start_col - 1), -1):
                result.append(matrix[end_row - 1][i])
            end_row -= 1

        # bottom to top
        if start_col < end_col:
            for i in range(end_row - 1, start_row - 1, -1):
                result.append(matrix[i][start_col])
            start_col += 1
        
    return result
    
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))