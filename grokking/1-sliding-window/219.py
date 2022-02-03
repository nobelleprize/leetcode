# https://leetcode.com/problems/contains-duplicate-ii/

def containsNearbyDuplicate(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= k:
            return True
        d[nums[i]] = i
    return False


print(containsNearbyDuplicate([1,2,3,1], 3
))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(containsNearbyDuplicate([99,99], 2))