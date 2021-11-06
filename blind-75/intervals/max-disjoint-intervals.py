def solution(intervals):
    intervals.sort(key = lambda x: x[1])
    result = 0

    a1 = intervals[0][1]

    for i in range(1, len(intervals)):
        b0 = intervals[i][0]
        b1 = intervals[i][1]

        if b0 >= a1:
            a1 = b1
        else:
            result += 1

    print(result)
        



# print(solution([[1,2], [2,3], [3,4], [1,3]]))
print(solution([[1,2], [1,2], [1,2]]))

# def solution(intervals):
#     intervals.sort(key = lambda x: x[1])
#     result = [[intervals[0]]]

#     a1 = intervals[0][1]

#     for i in range(1, len(intervals)):
#         b0 = intervals[i][0]
#         b1 = intervals[i][1]

#         if b0 > a1:
#             result.append([b0, b1])
#             a1 = b1
#     print(result)
        



# print(solution([[1,9], [2,3], [5,7]]))