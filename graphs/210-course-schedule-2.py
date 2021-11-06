# https://leetcode.com/problems/course-schedule-ii/
from collections import defaultdict

def findOrder(numCourses, prerequisites):
    d = dict()
    for i in range(numCourses):
        d[i] = []
    for i in prerequisites:
        d[i[1]].append(i[0])
    if all(len(value) > 0 for value in d.values()):
        return []

    return topologicalSort(d)

def topologicalSort(graph):
    visited = [0] * len(graph)
    stack = []

    for i in range(len(graph)):
        if visited[i] == 0:
            topologicalSortUtil(graph, i, visited, stack)
    if len(stack) != len(graph):
        return []
    return stack[::-1]

def topologicalSortUtil(graph, node, visited, stack):
    if visited[node] == 2:
        return []

    visited[node] = 2

    for i in graph[node]:
        if visited[i] == 0:
            if topologicalSortUtil(graph, i, visited, stack) == []:
                return []
        
        elif visited[i] == 2:
            return []
    
    visited[node] = 1
    stack.append(node)

    
# print(findOrder(3, [[1,2], [2,1]]))
# print(findOrder(3, [[0,1],[0,2],[1,2]]))
# print(findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(6, [[1,0], [2,0], [2,1], [3,2], [3,1], [4,2], [4,0], [4,3], [5,2], [5,4], [5,3]]))
