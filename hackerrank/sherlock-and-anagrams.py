# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
from collections import defaultdict
from email.policy import default

def sherlockAndAnagrams(s):
    d = defaultdict(int)

    for i in range(len(s)):
        for j in range(i, len(s)):
            cur = s[i:j + 1]
            cur = ''.join(sorted(cur))
            d[cur] += 1

    ans = 0
    for x in d:
        v = d[x]
        ans += (v * (v - 1)) // 2

    return ans

# print(checkAnagram("tsaco", "catzo"))
print(sherlockAndAnagrams("ifailuhkqq"))
print(sherlockAndAnagrams("kkkk"))