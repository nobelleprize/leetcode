# https://leetcode.com/problems/course-schedule/

def canFinish(numCourses, prerequisites):
    dictionary = dict()
    for i in range(0, numCourses):
        dictionary[i] = []
    for p in prerequisites:
        dictionary[p[0]].append(p[1])
        if p[1] in dictionary.keys():
            if p[0] in dictionary[p[1]]:
                return False
    
    if all(len(value) > 0 for value in dictionary.values()):
        return False

    visited = [0] * len(dictionary)

    for key, value in sorted(dictionary.items(), key=lambda x: len(x[1])):
        if canTake(dictionary, key, visited) == False:
            return False

    return True                

def canTake(dictionary, course, visited):
    if visited[course] == 2:
        return False
    
    visited[course] = 2

    for neighbor in dictionary[course]:
        if visited[neighbor] == 0:
            if canTake(dictionary, neighbor, visited) == False:
                return False
        elif visited[neighbor] == 2:
            return False
        
    visited[course] = 1
    return True


# print(canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
print(canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])) #true
# print(canFinish(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))
# print(canFinish(4, [[1,2], [2,3], [3,1]]))