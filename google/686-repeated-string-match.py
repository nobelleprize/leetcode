# https://leetcode.com/problems/repeated-string-match/
import math

def repeatedStringMatch(a, b):
    multiple = math.ceil(len(b) / len(a))
    if b in a*multiple:
        return multiple
    if b not in a*multiple:
        if b in a*(multiple+1):
            return multiple + 1
    return -1

# print(repeatedStringMatch(a = "abcd", b = "cdabcdab")) # 3
# print(repeatedStringMatch(a = "a", b = "aa")) # 2
# print(repeatedStringMatch(a = "a", b = "a")) # 1
# print(repeatedStringMatch(a = "abc", b = "wxyz")) # -1
# print(repeatedStringMatch("abc", "cab")) # 2
print(repeatedStringMatch("abc", "cabcabca"))