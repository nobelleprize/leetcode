# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
from collections import defaultdict

def numSplits(s):
    result = 0

    left = set()
    right = defaultdict(int)
    
    # left[s[0]] += 1
    left.add(s[0])

    for i in range(1, len(s)):
        right[s[i]] += 1
    
    for i in range(1, len(s)):
        if len(left) == len(right):
            result += 1
        left.add(s[i])
        right[s[i]] -= 1

        if right[s[i]] == 0:
            del right[s[i]]

    return result

print(numSplits("aacaba"))