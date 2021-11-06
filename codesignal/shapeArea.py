def shapeArea(n):
    if n == 1:
        return 1
    res = 0
    for i in range(1, n*2 -1, 2):
        res += i

    return res*2 + n*2 - 1

print(shapeArea(4))