# https://leetcode.com/problems/koko-eating-bananas/
import math

def minEatingSpeed(piles, h):
    piles.sort()
    left = 1
    right = piles[-1]
    while left < right:
        middle = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / middle)
        if hours <= h:
            right = middle
        else:
            left = middle + 1
    return right

# print(minEatingSpeed([3,6,7,11], 8)) # 4
# print(minEatingSpeed([30,11,23,4,20], 5)) # 30
# print(minEatingSpeed([30,11,23,4,20], 6)) # 23
print(minEatingSpeed([312884470], 312884469))