# https://leetcode.com/problems/3sum-closest/

def threeSumClosest(nums, target):
    nums.sort()
    diff = float("inf")

    for i in range(len(nums)):
        l = i+1
        r = len(nums) - 1
    
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if abs(sum - target) < abs(diff):
                diff = target - sum
            if sum < target:
                l += 1
            else:
                r -= 1
        if diff == 0:
            break
    return target - diff