# # https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s):
    if s == "":
        return 0
    max_len = 0
    seen = {}

    start = 0

    for i in range(len(s)):
        if s[i] in seen:

            start = max(start, seen[s[i]] + 1) 

        max_len = max(max_len, i - start + 1)
        seen[s[i]] = i

    return max_len


# # print(lengthOfLongestSubstring("bbbb")) #5
# # print(lengthOfLongestSubstring("abcabcbb")) # 3
# print(lengthOfLongestSubstring("pwwkew")) # 3
# # print(lengthOfLongestSubstring("dvdf")) # 3
# # print(lengthOfLongestSubstring("abcabcdeagh")) # 7


def lengthOfLongestSubstring(s):
    if s == "":
        return 0
    data = [0 for _ in range(len(s))]
    data[0] = 1

    seen = []
    seen.append(s[0])

    for i in range(1, len(s)):

        if s[i] not in seen:
            seen.append(s[i])
            data[i] = data[i-1] + 1

        else:
            seen = seen[seen.index(s[i])+1::]
            seen.append(s[i])
            data[i] = len(seen)

    return max(data)

# print(lengthOfLongestSubstring("abba")) #2
# print(lengthOfLongestSubstring("abcabcbb")) # 3
# print(lengthOfLongestSubstring("pwwkew")) # 3
# print(lengthOfLongestSubstring("dvdf")) # 3
# print(lengthOfLongestSubstring("abcabcdeagh")) # 7

