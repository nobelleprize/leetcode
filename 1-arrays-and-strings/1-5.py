# Given two strings, check if they are one (or zero) edits away

def one_away(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False
    short = s1 if len(s1) < len(s2) else s2
    long = s1 if len(s1) > len(s2) else s1
    
    foundDiff = False
    index1 = 0
    index2 = 0
    
    while index1 < len(short) and index2 < len(long):
        if short[index1] != long[index2]:
            if foundDiff:
                return False
            foundDiff = True

            if len(short) == len(long):
                index1 += 1
                # index2 += 1
        else:
            index1 += 1
        index2 += 1

    return True
            
       
# print(one_away("bale", "pale"))
# print(one_away("pale", "ple"))990000000000000
print(one_away("pales", "ple"))
