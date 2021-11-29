def score(s):
    d = {}
    score = 0
    for i in range(0, 10):
        d[str(i)] = set()

    for i in range(0, len(s)-1, 2):
        d[s[i+1]].add(s[i])
    
    for i in d.values():
        if i == {'R', 'G', 'B'}:
            score += 1
    return score

# print(score("B2R5G2R2"))


from collections import defaultdict

def longestPalindrome(A):
    d = defaultdict(int)
    result = 0
    doubles = []

    for i in A:
        d[i] += 1
    for key in d.keys():
        pal = key[::-1]
        if key[0] == key[1]:
            if d[key] % 2 == 0: # even
                result += d[key] * 2
            else: # odd
                doubles.append(d[key])
        elif pal in d:
            result += min(d[key], d[pal]) * 2
    doubles.sort()
    result += (doubles[-1] * 2)

    for i in doubles[0:-1]:
        if i % 2 == 1:
            result += ((i-1) * 2)

    return result

# print(longestPalindrome(["ck","kc","ho","kc","ck"]))
# print(longestPalindrome(["ck","kc","ho","kc"]))
# print(longestPalindrome(["ab","hu","ba","aa"]))
# print(longestPalindrome(["ra","ce","aa","bb", "aa", "ec","ar"]))
print(longestPalindrome(["bb",
                         "cc","cc","cc",
                         "dd","dd","dd","dd","dd",
                         "ee","ee","ee","ee","ee","ee","ee"]))