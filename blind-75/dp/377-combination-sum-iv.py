# https://leetcode.com/problems/combination-sum-iv/

# def solution(nums, target):
#     if target == 0:
#         return 1
#     res = 0
#     for i in range(len(nums)):
#         if target >= nums[i]:
#             res += solution(nums, target-nums[i])
#     return res

def solution(nums, target):
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    
    for i in range(len(dp)):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    print(dp[target])
    return dp[target]
    

solution([1, 2, 3], 4)