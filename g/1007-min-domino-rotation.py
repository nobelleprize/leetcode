# # https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

def minDominoRotations(tops, bottoms):
    n = len(tops)
    rotations = check(tops, bottoms, tops[0], n)

    if rotations != -1 or tops[0] == bottoms[0]:
        return rotations
    else:
        return check(tops, bottoms, bottoms[0], n)

def check(tops, bottoms, x, n):
    rotations_a = 0
    rotations_b = 0

    for i in range(n):
        if tops[i] != x and bottoms[i] != x:
            return -1
        elif tops[i] != x:
            rotations_a += 1
        elif bottoms[i] != x:
            rotations_b += 1
    
    return min(rotations_a, rotations_b)



# print(minDominoRotations(tops = [5,1,2,4,2,2], bottoms = [2,2,6,2,3,2]))

def minDominoRotations(tops, bottoms):
    res = checkDomino(tops, bottoms, tops[0])
    if res == -1:
        res = checkDomino(tops, bottoms, bottoms[0])
        if res == -1:
            return -1
        return res
    else:
        return res

def checkDomino(tops, bottoms, x):
    top_count = 0
    bottom_count = 0

    for i in range(len(tops)):
        if tops[i] != x and bottoms[i] != x:
            return -1
        elif tops[i] != x:
            top_count += 1
        elif bottoms[i] != x:
            bottom_count += 1
    return min(top_count, bottom_count)


print(minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))
        
        