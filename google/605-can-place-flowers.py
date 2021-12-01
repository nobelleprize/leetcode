# https://leetcode.com/problems/can-place-flowers/

def canPlaceFlowers(flowerbed, n):    
    if len(flowerbed) == 1 and n == 1 and flowerbed[0] == 0:
        return True
    for i in range(len(flowerbed)-1):
        if (i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0) or \
            (i == len(flowerbed) - 2 and flowerbed[i] == 0 and flowerbed[i+1] == 0) or \
                (flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
        if n <= 0:
            return True
    return n <= 0

# print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,0,1], 2))
# print(canPlaceFlowers([0,0,1,0,1], 1))
# print(canPlaceFlowers([0], 1))
print(canPlaceFlowers([0,0,0,0,0,1,0,0], 0))
