# https://leetcode.com/problems/course-schedule/
from collections import defaultdict

def canFinish(numCourses, prerequisites):
    d = dict()
    for i in range(numCourses):
        d[i] = []
    for p in prerequisites:
        d[p[0]].append(p[1])

    # if all(len(value) > 0 for value in d.values()):
        # return False

    taken = set()
    queue = []
    for key, value in d.items():
        if value != []:
            queue = value
        while queue:
            popped = queue.pop(0)

    print(d)

def canTake(d_courses, course):
    valid = set()
    visited = set()
    queue = d_courses[course]
    while queue:
        popped = queue.pop(0)
        if popped not in valid:
            visited.add(popped)
            

    return True

# print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))
