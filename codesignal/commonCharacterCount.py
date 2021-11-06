from collections import defaultdict

def commonCharacterCount(s1, s2):
    s1_dict = defaultdict(int)
    s2_dict = defaultdict(int) 
    for char in s1:
        s1_dict[char] += 1
    for char in s2:
        s2_dict[char] += 1 
    
    res = 0
    for key, value in s1_dict.items():
        if s2_dict[key]:
            res += min(s1_dict[key], s2_dict[key])
    return res

print(commonCharacterCount("aabcc", "adcaa"))
print(commonCharacterCount("aabcc", "adcaa"))