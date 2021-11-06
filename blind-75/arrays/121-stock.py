# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys

def solution(prices):
    min = sys.maxsize
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
        elif prices[i] - min > maxProfit:
            maxProfit = prices[i] - min
    return maxProfit


print(solution([7, 1, 5, 3, 6, 4]))
print(solution([7, 6, 4, 3, 1]))