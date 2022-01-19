# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

def longestIncreasingPath(matrix):
    if len(matrix) == 0:
        return 0

    cache = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result = max(result, traverse(matrix, i, j, cache))
    return result

def traverse(matrix, i, j, cache):
    if cache[i][j] != 0:
        return cache[i][j]

    dirs = [[-1,0], [1,0], [0,-1], [0,1]]
    for d in dirs:
        x = i + d[0]
        y = j + d[1]

        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
            cache[i][j] = max(cache[i][j], traverse(matrix, x, y, cache))
    
    return cache[i][j] + 1



print(longestIncreasingPath([[9,9,4],
                            [6,6,8],
                            [2,1,1]]))

# def longestIncreasingPath(matrix):
#     if len(matrix) == 0:
#         return 0
#     result = 0

#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             num = matrix[i][j]
#             result = max(result, traverse(matrix, i, j))
#     return result


# def traverse(matrix, i, j):
#     dirs = [[-1,0], [1,0], [0,-1], [0,1]]
#     result = 0
#     for x, y in dirs:
#         new_i = i + x
#         new_j = j + y

#         if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and matrix[new_i][new_j] > matrix[i][j]:
#             result = max(result, traverse(matrix, new_i, new_j))

#     return result + 1


# print(longestIncreasingPath([[9,9,4],
#                             [6,6,8],
#                             [2,1,1]]))

# print(longestIncreasingPath([[3,4,5],
#                             [3,2,6],
#                             [2,2,1]]))