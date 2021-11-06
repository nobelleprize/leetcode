# https://leetcode.com/problems/house-robber/

def solution(nums):
    if len(nums) == 0:
       return 0

    memo = [0 for i in range(len(nums) + 1)]
    memo[0] = 0
    memo[1] = nums[0]

    for i in range(1, len(nums)):
        memo[i+1] = max(memo[i], memo[i-1] + nums[i])
    
    return memo[len(nums)]


print(solution([1, 2, 3, 1]))