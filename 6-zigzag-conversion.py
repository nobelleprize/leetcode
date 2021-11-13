# https://leetcode.com/problems/zigzag-conversion/
from collections import defaultdict

def convert(s, numRows):
    if numRows == 1:
        return s
    count = 1
    addition = 1
    d = {}
    for i in range(1, numRows + 1):
        d[i] = []
    for i in range(len(s)):
        d[count].append(s[i])
        if count == 1:
            addition = 1
        if count == numRows:
            addition = 0
        if addition == 1:
            count += 1
        else:
            count -= 1
    res = ""

    for value in d.values():
        res += "".join(value)

    return res

# print(convert("PAYPALISHIRING", 3))
print(convert("AB", 1))