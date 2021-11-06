# https://leetcode.com/problems/search-in-rotated-sorted-array/

def solution(nums, target):
    i = nums[0]
    n = len(nums)
    if n == 1:
        if i == target:
            return 0
        return -1
    
    if i == target:
        return 0
    
    if i > target:
        for j in range(0, -n-1, -1):
            if nums[j] < target:
                return -1
            if nums[j] == target:
                return n+j
            if nums[j] > i:
                return -1

    if i < target:
        for j in range(0, n):
            if nums[j] > target:
                return -1
            if nums[j] == target:
                return j
            if nums[j] < i:
                return -1

    return -1 

print(solution([4, 5, 6, 7, 0, 1, 2], 0))
print(solution([3, 4, 5, 0, 1], 5))
print(solution([1, 3], 4))
print(solution([1], 1))
print(solution([1, 3], 1))
    
