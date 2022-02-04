# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    pointer = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[pointer]:
            pointer += 1
            nums[pointer] = nums[i]
    return pointer + 1


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))