# https://leetcode.com/problems/insert-interval/

def insert(intervals, newInterval):
    j = -1
    k = -1
    for i in range(len(intervals)):
        if isOverlap(intervals[i], newInterval):
            if j == -1:
                j = i
            k = i

    if j == -1:
        intervals.append(newInterval)
        return sorted(intervals)
    mini = min(intervals[j][0], newInterval[0])
    maxi = max(intervals[k][1], newInterval[1])
    
    return intervals[0:j] + [[mini, maxi]] + intervals[k+1:]


def isOverlap(a, b):
    if a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] or b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]:
        return True
    return False

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))