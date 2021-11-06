# courses =  [[1,0], [2,0], [2,1], [3,2], [3,1], [4,2], [4,0], [4,3], [5,2], [5,4], [5,3]]

def dfs(graph):
    visited = set()
    for i in graph:
        if i not in visited:
            dfsUtil(i, visited)

def dfsUtil(graph, node, visited):
    visited.add(node)
    print(node)
    for i in graph[node]:
        if i not in visited:
            dfsUtil(graph, i, visited)

def topologicalSort(graph):
    visited = [False] * len(graph)
    stack = []

    for i in range(len(graph)):
        if visited[i] == False:
            topologicalSortUtil(graph, i, visite, stack)
    
    print(stack[::-1])

def topologicalSortUtil(graph, node, visited, stack):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            topologicalSortUtil(graph, i, visited, stack)
    stack.append(node)