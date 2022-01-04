# https://leetcode.com/problems/trapping-rain-water/solution/

def trap(height):
    result = 0
    left_max = 0
    right_max = 0

    i = 0
    j = len(height) - 1
    
    while i <= j:
        
        if height[i] < height[j]:
            
            if height[i] > left_max:
                left_max = height[i]
            else:
                result += left_max - height[i]
            
            i += 1
        
        else:

            if height[j] > right_max:
                right_max = height[j]
            else:
                result += right_max - height[j]
            
            j -= 1
    return result

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))