# https://leetcode.com/problems/koko-eating-bananas/
import math

def minEatingSpeed(piles, h):
    piles.sort()
    left = 1
    right = piles[-1]
    while left < right:
        mid = (left + right) // 2
        
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    return right

# print(minEatingSpeed([3,6,7,11], 8))
# print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))