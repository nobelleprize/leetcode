# https://leetcode.com/problems/jump-game/

def canJump(nums):
    memo = [0 for _ in range(len(nums))]
    memo[-1] = True
    
    for i in range(len(nums)-1, -1, -1):
        furthestJump = min(i + nums[i], len(nums) - 1)
        for j in range(i, furthestJump+1):
            if memo[j] == True:
                memo[i] = True
                break
    print(memo)

    return memo[0] == True


# print(canJump([2,4,2,1,0,2,0]))
print(canJump([3,2,1,0,4]))