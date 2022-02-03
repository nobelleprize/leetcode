def lengthOfLongestSubstring(s):
    ans = 0
    sub = ''
    for char in s:
        if char not in sub:
            sub += char
            ans = max(ans, len(sub))
        else:
            cut = sub.index(char)
            sub = sub[cut+1:] + char
    return ans
    
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))