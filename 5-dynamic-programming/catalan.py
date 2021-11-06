# https://leetcode.com/problems/unique-binary-search-trees/

def solution(n):
    r = 1
    for i in range(1, n+1):
        r = r * coefficient(i)
    return r

def coefficient(i):
    return (2 * ((2 * i) - 1)) / (i + 1)

print(solution(3))