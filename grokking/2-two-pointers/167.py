# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target and l != r:
            return [l+1, r+1] 
        if numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1
    return [-1,-1]

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))

