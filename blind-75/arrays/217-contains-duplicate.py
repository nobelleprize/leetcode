# https://leetcode.com/problems/contains-duplicate/
from collections import defaultdict

def solution(nums):
    d = defaultdict(int)
    for num in nums:
        d[num] += 1
        if d[num] > 1:
            return True
    return False

print(solution([1, 2, 3, 1]))
print(solution([1, 2, 3, 4]))
print(solution([1, 1, 1, 3, 3, 4, 3, 2, 4, 25]))