# https://leetcode.com/problems/coin-change/

def coinChange(coins, amount):
    coinTable = [0] + [float('inf') for i in range(amount)]
    for i in range(1, amount+1):
        for coin in coins:
            if i-coin >= 0:
                coinTable[i] = min(coinTable[i], coinTable[i-coin]+1)
    if coinTable[-1] == float('inf'):
        return -1
    return coinTable[-1]

print(coinChange([1, 2, 5], 11))