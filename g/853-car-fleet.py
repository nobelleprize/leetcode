# https://leetcode.com/problems/car-fleet/

def carFleet(target, position, speed):
    sorted_pos_speed = sorted(zip(position, speed))
    time = [float(target - p) / s for p, s in sorted_pos_speed]
    res = 0
    cur = 0
    for t in time[::-1]:
        if t > cur:
            res += 1
            cur = t
    return res


print(carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,4,1,3]))