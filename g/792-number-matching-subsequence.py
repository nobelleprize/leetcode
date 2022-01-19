# https://leetcode.com/problems/number-of-matching-subsequences/
from collections import defaultdict

def numMatchingSubseq(s, words):
    d = defaultdict(int)
    s_dict = defaultdict(list)

    for i in range(len(s)):
        s_dict[s[i]].append(i)

    for word in words:
        d[word] += 1
    res = 0

    for word in d.keys():
        if len(word) <= len(s) and match(s_dict, word):
            res += d[word]
    return res


def match(s_dict, word):
    position = -1
    for i in range(len(word)):

        for j in s_dict[word[i]]:
            if all(x < position for x in s_dict[word[i]]):
                return False 
            if j > position:
                position = j


        if word[i] not in s_dict:
            return False
    return True

        


# print(match({'a': [0], 'b': [1], 'c': [2], 'd': [3, 5], 'e': [4]}, "aced")) # abcded
print(numMatchingSubseq("abcde", ["a","bb","acd","ace"]))
# print(numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))
# print(numMatchingSubseq("aaaaaaa", ["a"]))