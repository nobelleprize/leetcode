# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
 
# Library for INT_MAX
import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])


    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
            min = sys.maxsize
            for u in range(self.V):
                if dist[u] < min and sptSet[u] == False:
                    min = dist[u]
                    x = u
            sptSet[x] = True
 
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)
 
# Driver program
g = Graph(5)
g.graph = [[0, 6, 0, 1, 0], 
            [6, 0, 5, 2, 2], 
            [0, 5, 0, 0, 5], 
            [1, 2, 0, 0, 1], 
            [0, 2, 5, 1, 0]]
 
g.dijkstra(0);