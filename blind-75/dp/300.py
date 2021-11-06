def solution(nums):
    dp = [1 for _ in range(len(nums))]
    
    for i in range(1, len(dp)):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)

print(solution([10, 9, 2, 5, 3, 7, 101, 18]))