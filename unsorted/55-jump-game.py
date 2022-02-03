# https://leetcode.com/problems/jump-game/

def canJump(nums):
    pointer = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= pointer:
            pointer = i
    return pointer == 0

# print(canJump([2,4,2,1,0,2,0]))
print(canJump([3,2,1,0,4]))
# print(canJump([2, 3, 1, 1, 4]))