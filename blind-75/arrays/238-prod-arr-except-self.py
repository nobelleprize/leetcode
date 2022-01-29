# https://leetcode.com/problems/product-of-array-except-self/

def solution(nums):
    n = len(nums)
    result = [1] * n

    for i in range(1, n):
        result[i] = nums[i-1] * result[i-1]
    print(result)
    
    temp = 1
    for i in range(n-1, -1, -1):
        result[i] = result[i] * temp
        temp *= nums[i]
    return result



print(solution([1, 2, 3, 4]))