# https://leetcode.com/problems/fruit-into-baskets/
from collections import defaultdict

def totalFruit(fruits):
    d = defaultdict()
    i = 0
    j = 0
    result = 0
    while j < len(fruits):
        d[fruits[j]] = j
        j += 1

        if len(d) == 3:
            del_index = min(d.values())
            del d[fruits[del_index]]
            i = del_index + 1
        result = max(result, j-i)
    
    return result



# print(totalFruit([1,2,1])) # 3
# print(totalFruit([0,1,2,2])) # 3
# print(totalFruit([1,2,3,2,2])) # 4
# print(totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # 5
# print(totalFruit([1,0,1,4,1,4,1,2,3])) # 5
    