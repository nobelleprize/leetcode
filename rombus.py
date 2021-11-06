def solution(matrix, n):
    res = []
    working_radius = n - 1
    for i in range(working_radius, len(matrix) - working_radius ):
        for j in range(working_radius, len(matrix[0]) - working_radius ):  
            res.append(get_sum(matrix, i, j, n, working_radius))
    print(res)

        
def get_sum(matrix, i, j, n, working_radius):
    result = sum(matrix[i][j-working_radius:j+working_radius+1])
    temp = 1
    while temp <= working_radius:
        result += sum(matrix[i-temp][j-working_radius+temp:j+working_radius-temp+1])
        result += sum(matrix[i+temp][j-working_radius+temp:j+working_radius-temp+1])
        temp += 1
    return result



print(solution([[7, 2, 3, 2, 5, 7], 
                [1, 5, 6, 1, 7, 7], 
                [4, 2, 9, 4, 8, 7], 
                [7, 2, 3, 2, 5, 7], 
                [1, 5, 6, 1, 7, 7], 
                [4, 2, 9, 4, 8, 7]], 3))