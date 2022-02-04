# https://leetcode.com/problems/3sum/

def threeSum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i != 0 and nums[i-1] == nums[i]: # repeated i value
            continue
        l = i+1
        r = len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return result

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([]))
print(threeSum([0]))
print(threeSum([0,0,0,0]))