# https://leetcode.com/problems/climbing-stairs/

def climbingStairs(n):
    a = 1
    b = 2
    c = 0

    for i in range(2, n):
        c = a+b
        a = b
        b = c
        
    return c

print(climbingStairs(4))