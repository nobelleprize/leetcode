# https://leetcode.com/problems/find-if-path-exists-in-graph/
from collections import defaultdict

def validPath(edges, start, end):
    d = defaultdict(list)
    visited = [start]
    for edge in edges:
        d[edge[0]].append(edge[1])
        d[edge[1]].append(edge[0])
    queue = d[start]
    while len(queue) > 0:
        if end in queue:
            return True
        else:
            popped = queue.pop(0)
            visited.append(popped)
            for i in d[popped]:
                if i not in visited:
                    queue.append(i)
    return False


# print(validPath( [[0,1], [3,4], [2,3],  [1,2], [4,0]], 0, 4 ))
# print(validPath([[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
print(validPath([[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5))