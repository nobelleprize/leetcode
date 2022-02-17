# https://leetcode.com/problems/bus-routes/
from collections import defaultdict

def numBusesToDestination(routes, source, target):
    routes = map(set, routes)
    routes = list(routes)
    if source == target: 
        return 0

    graph = defaultdict(set)
    for i in range(len(routes)):
        for j in range(i+1, len(routes)):
            r1 = routes[i]
            r2 = routes[j]
            if any(r in r2 for r in r1):
                graph[i].add(j)
                graph[j].add(i)
    
    seen = set()
    targets = set()
    for i in range(len(routes)):
        if source in routes[i]:
            seen.add(i)
        if target in routes[i]:
            targets.add(i)
        
    queue = [(node,1) for node in seen]
    for node, depth in queue:
        if node in targets:
            return depth
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, depth+1))
    return -1

print(numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))