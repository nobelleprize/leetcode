# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
    intervals.sort()
    result = [intervals[0]]
    intervals.pop(0)

    while len(intervals) > 0:
        last = result[-1]
        if last[1] >= intervals[0][0]:
            result[-1] = [last[0], max(last[1], intervals[0][1])]
            intervals.pop(0)
        else:
            result.append(intervals.pop(0))
    return result

        # popped = intervals.pop(0)
        # if len(intervals) == 0:

        # if popped[1] > intervals[0][0] and popped[0] <= intervals[0][1]:
        #     res = [popped[0], max(popped[1], intervals[0][1])]
        #     result.append(res)
        #     intervals.pop(0)
        # else:
        #     result.append(popped)
    print(result)

# print(merge([[1,3],[8,10],[2,6],[15,18]])) # [[1,6],[8,10],[15,18]]
# print(merge([[1,4],[4,5]])) # [[1,5]]
print(merge([[1,4],[0,4]])) #[[0,4]]