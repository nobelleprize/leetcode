# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import defaultdict

def findAnagrams(s, p):
    result = []
    pCount = defaultdict(int)
    sCount = defaultdict(int)

    for char in p:
        pCount[char] += 1
    
    for i in range(len(s)):
        sCount[s[i]] += 1

        if i >= len(p):

            if sCount[s[i - len(p)]] == 1:
                del sCount[s[i - len(p)]]
            else:
                sCount[s[i - len(p)]] -= 1
        
        if pCount == sCount:
            result.append(i - len(p) + 1)
    return result

print(findAnagrams("cbaebabacd", "abc"))