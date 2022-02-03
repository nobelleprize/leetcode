# https://leetcode.com/problems/asteroid-collision/

def asteroidCollision(asteroids):
    stack = []
    for rock in asteroids:
        while stack and rock < 0 and stack[-1] > 0:
            previous = stack.pop()
            if previous > -rock:
                rock = previous
            elif previous == -rock:
                rock = 0
        if rock:
            stack.append(rock)
    return stack


print(asteroidCollision([5,10,-5]))
print(asteroidCollision([10,2,-5]))