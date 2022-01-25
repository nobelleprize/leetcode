# https://leetcode.com/problems/asteroid-collision/

def asteroidCollision(asteroids):
    result = []
    for ast in asteroids:
        while result and result[-1] > 0 and ast < 0:
            if result[-1] < -ast:
                result.pop()
                continue
            elif result[-1] == -ast:
                result.pop()
            break
        else:
            result.append(ast)
    return result

# print(asteroidCollision([5, 10, -5])) # 5,10
# print(asteroidCollision([8, -8])) # []
# print(asteroidCollision([10, 2, -5])) # 10
# print(asteroidCollision([-2,-1,1,2])) # -2, -1, 1, 2
# print(asteroidCollision([-2,-2,1,-2])) # -2, -2, -2 
# print(asteroidCollision([-2,1,1,-1])) # -2, 1
print(asteroidCollision([1, 2, 3, -1, -2]))