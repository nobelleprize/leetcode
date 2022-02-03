# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
import itertools

def letterCombinations(digits):
    if digits == "":
        return []
        
    d = {'2': ['a','b','c'],
         '3': ['d','e','f'],
         '4': ['g','h','i'],
         '5': ['j','k','l'],
         '6': ['m','n','o'],
         '7': ['p','q','r','s'],
         '8': ['t','u','v'],
         '9': ['w','x','y','z']}
         
    reduced = []
    for num in digits:
        reduced.append(d[num])

    return list(map("".join, itertools.product(*reduced)))



print(letterCombinations("23"))
# print(letterCombinations("2"))