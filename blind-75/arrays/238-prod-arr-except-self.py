# https://leetcode.com/problems/product-of-array-except-self/

def solution(nums):
    # n = len(nums)
    # prefix = [0]*n
    # suffix = [0]*n

    # result = [0]*n

    # prefix[0] = 1
    # suffix[-1] = 1

    # for i in range(1, n):
    #     prefix[i] = prefix[i-1]*nums[i-1]

    # for i in range(n-2, -1, -1):
    #     suffix[i] = suffix[i+1]*nums[i+1]

    # for i in range(n):
    #     result[i] = prefix[i]*suffix[i]
    # print("stop")

    n = len(nums)
    result = [1] * n
    temp = 1
    for i in range(n):
        result[i] = temp
        temp = temp * nums[i]
    temp = 1
    for i in range(n-1, -1, -1):
        result[i] = result[i] * temp
        temp = temp * nums[i]
    return result



print(solution([1, 2, 3, 4]))