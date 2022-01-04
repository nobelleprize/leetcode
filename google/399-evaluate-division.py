# https://leetcode.com/problems/evaluate-division/
from collections import defaultdict

def calcEquation(equations, values, queries):
    graph = defaultdict(defaultdict)

    for i in range(len(equations)):
        first = equations[i][0]
        second = equations[i][1]
        graph[first][second] = values[i]
        graph[second][first] = 1 / values[i]
    print(graph)
    
    results = []
    for first, second in queries:
        if first not in graph or second not in graph:
            results.append(-1)
        elif first == second:
            results.append(1)
        else:
            visited = set()
            cache = defaultdict(defaultdict)

            results.append(traverse(graph, first, second, 1, visited, cache))
            
            temp = graph.copy()
            graph.update(cache)
            graph.update(temp)
    return results

def traverse(graph, curr, target, product, visited, cache):
    cache[curr][target] = product
    visited.add(curr)
    result = -1
    neighbors = graph[curr]
    if target in neighbors:
        result = product * neighbors[target]
    else:
        for neighbor, value in neighbors.items():
            print(neighbor, value)
            if neighbor in visited:
                continue
            result = traverse(graph, neighbor, target, product * value, visited, cache)
            if result != -1:
                break
    return result



print(calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], 
    values = [1.5,2.5,5.0], 
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))

# print(calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

# print(calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
# [3.0,4.0,5.0,6.0],
# [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
# ))