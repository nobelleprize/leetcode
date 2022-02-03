# https://leetcode.com/problems/repeated-dna-sequences/

def findRepeatedDnaSequences(s):
    seen = set()
    result = set()
    for i in range(len(s) - 10 + 1):
        tmp = s[i : i + 10]
        if tmp in seen:
            result.add(tmp)
        seen.add(tmp)
    return list(result)

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))