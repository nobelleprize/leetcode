def mergeIntervals(intervals):
    if len(intervals) == 1:
        return intervals

    l = len(intervals)
    intervals.sort()
    i = 0
    popped = 0

    while i + popped < l-1:
        if isOverlap(intervals[i], intervals[i+1]):
            intervals[i][0] = intervals[i][0] #if intervals[i][0] < intervals[i+1][0] else intervals[i+1][0]
            intervals[i][1] = intervals[i][1] if intervals[i][1] > intervals[i+1][1] else intervals[i+1][1]
            intervals.pop(i+1)
            popped += 1
        else:
            i += 1

    return intervals 


def isOverlap(a, b):
    if a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] or b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]:
        return True
    return False

print(mergeIntervals([[1, 3], [2, 2], [2, 2], [2, 3], [3, 3], [4, 6], [5, 7]]))
    