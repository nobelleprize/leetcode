# https://leetcode.com/problems/campus-bikes/
import heapq

def assignBikes(workers, bikes):
    distances = []
    for i, worker in enumerate(workers):
        for j, bike in enumerate(bikes):
            distance = manhattanDistance(worker, bike)
            distances.append((distance, i, j))
    
    distances.sort()
    result = [-1] * len(workers)
    bike_taken = set()
    for distance, i, j, in distances:
        if result[i] == -1 and j not in bike_taken:
            result[i] = j
            bike_taken.add(j)
        if len(bike_taken) == len(workers):
            break

    return result

def assignBikesHeap(workers, bikes):
    distances = []    
    for i, (x, y) in enumerate(workers):
        distances.append([])
        for j, (x_b, y_b) in enumerate(bikes):
            distance = abs(x - x_b) + abs(y - y_b)
            distances[-1].append((distance, i, j))
        distances[-1].sort(reverse = True) 
    print(distances)

    result = [None] * len(workers)
    used_bikes = set()
    queue = [distances[i].pop() for i in range(len(workers))]   
    heapq.heapify(queue)

    while len(used_bikes) < len(workers):
        _, worker, bike = heapq.heappop(queue)
        if bike not in used_bikes:
            result[worker] = bike
            used_bikes.add(bike)
        else:
            heapq.heappush(queue, distances[worker].pop()) 

    return result

def manhattanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

print(assignBikesHeap(workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]))
# print(assignBikesHeap(workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]])) # 0, 2, 1