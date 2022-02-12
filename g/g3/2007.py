# https://leetcode.com/problems/find-original-array-from-doubled-array/
from collections import Counter

def findOriginalArray(changed):
    c = Counter(changed)
    if c[0] % 2:
        return []
    for x in sorted(c):
        if c[x] > c[2 * x]:
            return []
        if x:
            c[2*x] -= c[x]
        else: # x == 0
            c[x] -= c[x] // 2
    return list(c.elements())

print(findOriginalArray([0,0,0,0,0,0,0,0,0,0]))