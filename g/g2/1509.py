# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
import heapq

def minDifference(nums):
    if len(nums) <= 3:
        return 0
        
    smallest = heapq.nsmallest(4, nums)
    largest = heapq.nlargest(4, nums)

    return min(
        largest[0]-smallest[-1],
        largest[1]-smallest[-2],
        largest[2]-smallest[-3],
        largest[3]-smallest[-4],
    )

print(minDifference([5,3,2,4]))
print(minDifference([1,5,0,10,14]))
print(minDifference([1,2,3,4,5,6]))