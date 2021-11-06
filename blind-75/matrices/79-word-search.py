def exist(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                if existUtil(board, word, row, col, 0):
                    return True
    return False

def existUtil(board, word, row, col, i):
    if i == len(word):
        return True

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or \
            board[row][col] != word[i]:
        return False

    if board[row][col] == word[i]:
        temp = board[row][col]
        board[row][col] = '*'

        res = (existUtil(board, word, row-1, col, i+1) | 
        existUtil(board, word, row+1, col, i+1) |
        existUtil(board, word, row, col+1, i+1) |
        existUtil(board, word, row, col-1, i+1))

        board[row][col] = temp
        return res
    else:
        return False



# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
# print(exist( [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))