# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from collections import defaultdict

def findSubstring(s, words):
    result = []
    word_length = len(words[0])
    substr_length = len(words[0]) * len(words)
    word_count = defaultdict(int)

    for word in words:
        word_count[word] += 1

    for i in range(len(s) - substr_length + 1):
        if check(s, i, word_count.copy(), substr_length, word_length, len(words)):
            result.append(i)
    return result

def check(s, i, remaining, substr_length, word_length, k):
    words_used = 0

    for j in range(i, i + substr_length, word_length):
        sliced = s[j : j + word_length]
        
        if remaining[sliced] > 0:
            remaining[sliced] -= 1
            words_used += 1
        
        else:
            break
    
    return words_used == k

print(findSubstring("barfoothefoobarman", ["foo","bar"]))
print(findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))
print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))