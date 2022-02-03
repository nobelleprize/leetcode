# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

def minimumDeletions(nums):
    deletions = len(nums)
    index_mini = nums.index(min(nums))
    index_maxi = nums.index(max(nums))
    maxi = max(index_mini, index_maxi)
    mini = min(index_mini, index_maxi)

    if maxi + 1 < deletions:
        deletions = maxi + 1

    if len(nums[mini:]) < deletions:
        deletions = len(nums[mini:])

    if len(nums[:mini])+1 + len(nums[maxi:]) < deletions:
        deletions = len(nums[:mini])+1 + len(nums[maxi:])

    return deletions

print(minimumDeletions([2,10,7,5,4,1,8,6]))
print(minimumDeletions(nums = [0,-4,19,1,8,-2,-3,5]))
print(minimumDeletions([101]))