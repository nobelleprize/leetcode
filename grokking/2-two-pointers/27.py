# https://leetcode.com/problems/remove-element/

def removeElement(nums, val):
    p = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[p] = nums[i]
            p += 1
    return p

print(removeElement([3,2,2,3], 3))
