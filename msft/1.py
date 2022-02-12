# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    d = dict()
    for i in range(len(nums)):
        x = target - nums[i]
        if x in d:
            return [i, d[x]]
        d[nums[i]] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))