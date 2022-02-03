# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    result = 0
    sub = ""
    for char in s:
        if char not in sub:
            sub += char
            result = max(len(sub), result)
        else:
            char_index = sub.index(char)
            sub = sub[char_index+1:] + char
    return result


print(lengthOfLongestSubstring("pwwkew"))