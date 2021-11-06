# https://leetcode.com/problems/find-center-of-star-graph/
from collections import defaultdict

def findCenter(edges):
    center = edges[0]
    for i in range(1,len(edges)):
        if center[1] == edges[i][0] or center[1] == edges[i][1]:
            center[0] = center[1]
    return center[0]



print(findCenter([[1,2],[5,1],[1,3],[1,4]]))