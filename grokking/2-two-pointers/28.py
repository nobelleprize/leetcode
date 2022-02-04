# https://leetcode.com/problems/implement-strstr/

def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1

# print(strStr("hello", "ll"))
# print(strStr("tacocat", "cat"))
print(strStr("", ""))