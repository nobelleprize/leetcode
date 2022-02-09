# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(nums):
    j = 1
    count = 1
    for i in range(1, len(nums)):
        
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 0
        
        if count <= 2:
            nums[j] = nums[i]
            j += 1
    return j

print(removeDuplicates([1,1,1,2,2,3]))