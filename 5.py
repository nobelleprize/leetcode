# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s):
    res = ""
    
    for i in range(len(s)):
            # odd case
            odd = expand(s, i, i)
            if len(odd) > len(res):
                res = odd

            # even case
            even = expand(s, i, i + 1)
            if len(even) > len(res):
                res = even
    return res

def expand(s, l, r):
    while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]



print(longestPalindrome("xxxxtacocat"))