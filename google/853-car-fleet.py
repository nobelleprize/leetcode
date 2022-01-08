# https://leetcode.com/problems/car-fleet/
from collections import defaultdict

def carFleet(target, position, speed):
    fleets = len(position)

    d = defaultdict(list)
    
    for i in range(target + 1):
        d[i] = []
    for i in range(len(position)):
        d[position[i]].append(speed[i])

    # print(d)
    positions = sorted(position)

    while len(d[target]) < len(position) - 1:

        for i in range(len(positions)):
            speed = d[positions[i]].pop()
            
            if i == len(position) - 2:
                new_pos = positions[i] + speed
            else:
                new_pos = min(positions[i+1], positions[i] + speed)

            if new_pos == positions[i+1]:
                positions.pop(0)
                fleets -= 1
        print(fleets)

    return fleets
        

            
            # if positions[i] + speed >= positions[i+1]:



print(carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,4,1,3]))