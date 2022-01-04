# https://leetcode.com/problems/find-and-replace-in-string/

def findReplaceString(s, indices, sources, targets):
    source = sorted(zip(indices, sources, targets))
    result = s[0:source[0][0]]
    
    for i in range(len(source)):
        item = source[i]
        begin = item[0]
        source_len = len(item[1])
        end = item[0] + source_len

        if s[begin:end] == item[1]:
            result += item[2]
        else:
            result += s[begin:end]

        if i != len(indices)-1 and end < source[i+1][0]:
            result += s[end:source[i+1][0]]
    if end <= len(s) - 1:
        result += s[end:]

    return result

print(findReplaceString("reauaqyxle",
[4,6,2],
["aq","yxl","au"],
["c","dh","ev"]))
# "reevcdhe"


# print(findReplaceString(s = "vmokgggqzp",
#                         indices = [3,5,1], 
#                         sources = ["kg","ggq","mo"], 
#                         targets = ["s","so","bfr"]))
# # "vbfrssozp"

# print(findReplaceString(s = "abcd", 
#                         indices = [0, 2], 
#                         sources = ["a", "cd"], 
#                         targets = ["eee", "ffff"]))
# # # eee b ffff

# print(findReplaceString(s = "abcd",
#                         indices = [0, 2], 
#                         sources = ["ab","ec"], 
#                         targets = ["eee","ffff"]))
# # eeecd