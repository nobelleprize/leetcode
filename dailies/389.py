# https://leetcode.com/problems/find-the-difference/

def findTheDifference(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    i = 0
    while i < len(s):
        if sorted_s[i] != sorted_t[i]:
            return sorted_t[i]
        i += 1

    return sorted_t[i]

print(findTheDifference("abcd", "abcde"))