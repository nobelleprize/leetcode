def isSubsetSum(set, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False
    
    if set[n-1] > sum:
        return isSubsetSum(set, n-1, sum)

    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])

print(isSubsetSum([3, 4, 5, 2], 4, 9))