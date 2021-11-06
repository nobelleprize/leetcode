# Given two strings, determine if s2 is a rotation of s1 using only one call to isSubstring ("waterbottle" is a rotation of "erbottlewat")

def string_rotation(s1: str, s2: str) -> bool:
    return (s2*2).find(s1) != -1

print(string_rotation("waterbottle", "erbottlewat"))
print(string_rotation("waterbottle", "cat")) 