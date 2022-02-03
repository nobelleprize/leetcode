# https://leetcode.com/problems/longest-string-chain/
from collections import defaultdict

def longestStrChain(words):
    words.sort(key=len)
    result = 0
    d = defaultdict(int)

    for word in words:
        d[word] = 1
        
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]
            
            if predecessor in d and d[predecessor] + 1 > d[word]:
                d[word] = d[predecessor] + 1
            
            result = max(result, d[word])
    
    return result

print(longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))