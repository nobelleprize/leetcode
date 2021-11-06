# https://leetcode.com/problems/two-sum/

def solution(nums, target):
    d = dict()
    for count, value in enumerate(nums):
        x = target - value
        if x in d:
            return [count, d[x]]
        d[value] = count


# print(solution([2, 7, 11, 15], 9))
print(solution([3, 2, 4], 6))