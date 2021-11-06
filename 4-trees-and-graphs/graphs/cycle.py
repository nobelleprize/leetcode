from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # def isCyclic(self):
    #     visited = [False] * self.V
    #     recStack = [False] * self.V
    #     for node in range(self.V):
    #         if visited[node] == False:
    #             if self.isCyclicUtil(node, visited, recStack) == True:
    #                 return True
    #     return False

    # def isCyclicUtil(self, node, visited, recStack):
    #     visited[node] = True
    #     recStack[node] = True
        
    #     for neighbor in self.graph[node]:
    #         if visited[neighbor] == False:
    #             if self.isCyclicUtil(neighbor, visited, recStack) == True:
    #                 return True
    #         elif recStack[node] == True:
    #             return True
        
    #     recStack[node] = False
    #     return False


    def isCyclicUndirected(self):
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] == False:
                if self.isCyclicUndirectedUtil(i, visited, -1):
                    return True
        return False
    
    def isCyclicUndirectedUtil(self, node, visited, parent):
        visited[node] = True
        for i in self.graph[node]:
            if visited[i] == False:
                if self.isCyclicUndirectedUtil(i, visited, node) == True:
                    return True
            elif parent != i:
                return True
        return False


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

print(g.isCyclicUndirected())