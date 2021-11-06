def isLucky(n):
    half = len(str(n)) // 2
    res1 = 0
    res2 = 0
    for i in range(0, half):
        res1 += n % 10
        n = n // 10
    while n != 0:
        res2 += n % 10
        n = n // 10

    return res1 == res2

print(isLucky(239017))