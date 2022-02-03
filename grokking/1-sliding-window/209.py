# https://leetcode.com/problems/minimum-size-subarray-sum/

def minSubArraylen(target, nums):
    result = float("inf")
    left = 0
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]
        while sum >= target:
            result = min(result, i - left + 1) # i - left + 1 is size of subarray
            sum -= nums[left]
            left += 1
            
    return result if result != float("inf") else 0


print(minSubArraylen(7, [2,3,1,2,4,3]))
print(minSubArraylen(4, [1,4,4]))