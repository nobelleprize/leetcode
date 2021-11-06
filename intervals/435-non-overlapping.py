# https://leetcode.com/problems/non-overlapping-intervals/
from collections import defaultdict

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x:x[1])
    i = 0
    j = 1
    counter = 0
    l = len(intervals)
    while j < l:
        if intervals[i][1] > intervals[j][0]:
            counter += 1
        else:
            i = j
        j += 1
    return counter


# def isOverlap(a, b):
#     if a[0] < b[0] < a[1] or a[0] < b[1] < a[1] or b[0] < a[0] < b[1] or b[0] < a[1] < b[1]:
#         return True
#     return False

print(eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
))
# print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
# print(eraseOverlapIntervals([[1,2], [3,5], [3,6], [4,5], [5,7], [8,11], [9,10]]))