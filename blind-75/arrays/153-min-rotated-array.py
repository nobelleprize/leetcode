# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def solution(nums):
    for i in range(len(nums)):
        if nums[i-1] > nums[i]:
            return nums[i]

    return 0

print(solution([3, 4, 5, 1, 2]))
print(solution([4, 5, 6, 7, 0, 1, 2]))
print(solution([11, 13, 15, 17]))