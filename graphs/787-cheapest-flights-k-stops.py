# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import heapq

def findCheapestPrice(n, flights, src, dst, k):
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for src, dest, cost in flights:
        adj_matrix[src][dest] = cost
    
    distances = [float('inf') for _ in range(n)]
    stops_arr = [float('inf') for _ in range(n)]
    distances[src] = 0
    stops_arr[src] = 0

    heap = [(0,0,src)] # cost, stops, node

    while heap:
        cost, stops, node = heapq.heappop(heap)
        
        if node == dst:
            return cost
        
        if stops == k + 1:
            continue
        
        for neighbor in range(n):
            if adj_matrix[node][neighbor] > 0:
                dU = cost
                dV = distances[neighbor]
                wUV = adj_matrix[node][neighbor]

                if dU + wUV < dV:
                    distances[neighbor] = dU + wUV
                    heapq.heappush(heap, ((dU + wUV), (stops + 1), neighbor))

                elif stops < stops_arr[neighbor]:
                    heapq.heappush(heap, ((dU + wUV), (stops + 1), neighbor))
                
                stops_arr[neighbor] = stops
    
    if distances[dst] == float('inf'):
        return -1
    return distances[dst]


print(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))