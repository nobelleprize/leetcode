# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    result = 0
    l = 0
    r = len(height) - 1
    
    while l < r:
        result = max(result, (r-l)*min(height[l], height[r]))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return result

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))