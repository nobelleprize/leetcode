# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
from collections import defaultdict

# def removeStones(stones):
#     row_rep = {}
#     col_rep = {}
#     graph = {}
#     for x, y in stones:
#         if x not in row_rep:
#             row_rep[x] = (x,y)
#         if y not in col_rep:
#             col_rep[y] = (x,y)
#         graph[(x,y)] = []
#         if row_rep[x] != (x,y):
#             graph[row_rep[x]].append((x,y))
#             graph[(x,y)].append(row_rep[x])
#         if col_rep[y] != (x,y):
#             graph[col_rep[y]].append((x,y))
#             graph[(x,y)].append(col_rep[y])
#     islands = 0
#     visited = set()
#     for x, y in stones:
#         if (x, y) not in visited:
#             dfs(x, y, graph, visited)
#             islands += 1
#     return len(stones) - islands

# def dfs(x, y, graph, visited):
#     visited.add((x,y))
#     for neigh_x, neigh_y in graph[(x,y)]:
#         if (neigh_x, neigh_y) not in visited:
#             dfs(neigh_x, neigh_y, graph, visited)

# # print(removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
# print(removeStones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]))

def removeStones(stones):
    points = {(i, j) for i, j in stones}
    island = 0
    rows = defaultdict(list)
    cols = defaultdict(list)
    for i, j in stones:
        rows[i].append(j)
        cols[j].append(i)
    for i, j in stones:
        if (i, j) in points:
            dfs(points, rows, cols, (i, j))
            island += 1
    return len(stones) - island

def dfs(points, rows, cols, point):
    points.discard(point)
    for y in rows[point[0]]:
        if (point[0], y) in points:
            dfs(points, rows, cols, (point[0], y))
    for x in cols[point[1]]:
        if (x, point[1]) in points:
            dfs(points, rows, cols, (x, (point[1])))


print(removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
# print(removeStones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]))
