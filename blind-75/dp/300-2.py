
def lengthOfLIS(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = 1
    result = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
            else:
                dp[i] = max(dp[i], 1)
        result = max(result,dp[i])
    print(dp)
    return max(dp)


print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7]))
# print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))