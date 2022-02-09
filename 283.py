# https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    pos = 0
    
    for i in range(len(nums)):
        elem = nums[i]
        if elem != 0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
    return nums
print(moveZeroes([0,1,0,3,12]))