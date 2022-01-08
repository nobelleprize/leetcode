# https://leetcode.com/problems/fruit-into-baskets/
from collections import defaultdict

def totalFruit(fruits):
    d = defaultdict(int)
    
    result = 0
    j = 0
    
    for i in range(len(fruits)):
        d[fruits[i]] = i

        if len(d) == 3:
            del_index = min(d.values())
            del d[fruits[del_index]]
            j = del_index + 1

        result = max(result, i-j+1)

    return result



# print(totalFruit([1,2,1])) # 3
# print(totalFruit([0,1,2,2])) # 3
# print(totalFruit([1,2,3,2,2])) # 4
# print(totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # 5
# print(totalFruit([1,0,1,4,1,4,1,2,3])) # 5
    