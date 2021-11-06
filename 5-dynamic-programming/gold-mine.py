def getMaxGold(gold, n, m):

    for col in range(n-2, -1, -1):
        for row in range(m):

            if row == 0:
                right_up = 0
            else:
                right_up = gold[row-1][col+1]

            if row == n-1:
                right_down = 0
            else:
                right_down = gold[row+1][col+1]
        
            if col == m-1:
                right = 0
            else:
                right = gold[row][col+1]
            
            gold[row][col] = gold[row][col] + max(right, right_up, right_down)

    res = gold[0][0]
    for i in range(1, m):
        res = max(res, gold[i][0])
    return res
# Driver code
gold = [[1, 3, 3],
        [2, 1, 4],
        [0, 6, 4]]
 
n = 3
m = 3
 
print(getMaxGold(gold, n, m))