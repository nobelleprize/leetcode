# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
from collections import defaultdict

def numSplits(s):
    result = 0
    left = set()
    right = defaultdict(int)
    for i in s:
        right[i] += 1
    
    for i in s:
        left.add(i)
        right[i] -= 1
        if right[i] == 0:
            del right[i]
        if len(left) == len(right.keys()):
            result += 1
    return result

print(numSplits("aacaba"))
