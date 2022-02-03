# https://leetcode.com/problems/container-with-most-water/

def areaMax(height):
    l = 0
    r = len(height) - 1
    area = 0
     
    while l < r:
        area = max(area, min(height[l], height[r]) * (r - l))
     
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return area


# print(areaMax([1,8,6,2,5,4,8,25,7]))    # 49
# print(areaMax([1,8,6,2,5,4,8,3,7])) # 49
# print(areaMax([4,3,2,1,4])) # 16
print(areaMax([2,3,4,5,18,17,6]))