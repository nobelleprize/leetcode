#           Graphs
# BFS

def BFS(graph, node):
    visited = [False] * len(graph)
    queue = []

    queue.append(node)
    visited[node] = True

    while queue:
        node = queue.pop(0)
        
        print(node)

        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


# DFS
# Connected
def DFS(graph, node):
    visited = set()
    DFSUtil(graph, node, visited)

def DFSUtil(graph, node, visited):
    visited.add(node)
    
    print(node)

    for i in graph[node]:
        if i not in visited:
            DFSUtil(i, visited)

# disconnected
def DFS(graph):
    visited = set()
    for i in graph:
        if i not in visited:
            DFSUtil(i, visited)

def DFSUtil(graph, node, visited):
    visited.add(node)

    print(node)

    for i in graph[node]:
        if i not in visited:
            DFSUtil(graph, i, visited)



# detect cycle
def isCyclic(graph):
    visited = [False] * len(graph)
    recStack = [False] * len(graph)

    for i in range(len(graph)):
        if visited[i] == False:
            if isCyclicUtil(graph, i, visited, recStack) == True:
                return True
    return False

def isCyclicUtil(graph, node, visited, recStack):
    visited[node] = True
    recStack[node] = True

    for i in graph[node]:
        if visited[i] == False:
            if isCyclicUtil(i, visited, recStack) == True:
                return True
        elif recStack[i] == True:
            return True

    recStack[node] = False
    return False


# topological sort

def topologicalSort(graph):
    visited = [False] * len(graph)
    stack = []

    for i in range(len(graph)):
        if visited[i] == False:
            topologicalSortUtil(graph, i, visited, stack)

    print(stack[::-1])

def topologicalSortUtil(graph, node, visited, stack):
    visited[node] = True

    for i in graph[node]:
        if visited[i] == False:
            topologicalSortUtil(graph, i, visited, stack)

    stack.append(node)
