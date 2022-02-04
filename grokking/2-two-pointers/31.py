# https://leetcode.com/problems/next-permutation/

def nextPermutation(nums):
    i = len(nums)-1
    j = len(nums)-1

    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    if i == 0:   # nums are in descending order
        nums.reverse()
        return 

    i -= 1    # find the last "ascending" position
    while nums[j] <= nums[i]:
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]  

    # reverse right half
    l = i + 1
    r = len(nums) -1 
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 
        r -= 1
    
    return nums
    
print(nextPermutation([1,2,3]))
# print(nextPermutation([1,5,8,4,7,5,5,3,1]))
# print(nextPermutation([1,5,8,7,6,5,4,3,2,1]))
# print(nextPermutation([3,2,1]))
