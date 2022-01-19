# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
import sys

def minDifference(nums):
    nums.sort()
    mini = sys.maxsize
    
    # kill 3 beginning
    arr_a = nums[3::]
    if arr_a[-1] - arr_a[0] < mini:
        mini = arr_a[-1] - arr_a[0]
    
    # kill 3 ending
    arr_b = nums[0:-3]
    if arr_b[-1] - arr_b[0] < mini:
        mini = arr_b[-1] - arr_b[0]
    
    # kill 2, 1
    arr_c = nums[2:-1]
    if arr_c[-1] - arr_c[0] < mini:
        mini = arr_c[-1] - arr_c[0]

    # kill 1, 2
    arr_d = nums[1:-2]
    if arr_d[-1] - arr_d[0] < mini:
        mini = arr_d[-1] - arr_d[0]

    print(mini)

# def solution2(nums):
#     if len(nums) <= 4:
#         return 0
    
#     nums.sort()
#     sz = len(nums)
#     val1 = nums[sz - 4] - nums[0]
#     val2 = nums[sz - 3] - nums[1]
#     val3 = nums[sz - 2] - nums[2]
#     val4 = nums[sz - 1] - nums[3]
#     return min(val1, val2, val3, val4)

    
    


# print(minDifference([5,3,2,4]))
print(minDifference([1,5,0,10,14]))
# print(minDifference([6,6,0,1,1,4,6]))
# print(minDifference([82,81,95,75,20]))
# print(solution2([9,48,92,48,81,31]))

