# https://leetcode.com/problems/word-break/

def solution(s, wordDict):
    n = len(s)
    dp = [False for i in range(n + 1)]
    dp[0] = True
    for i in range(1, n + 1):
        for word in wordDict:
            test = dp[i-len(word)]
            if dp[i - len(word)] and word == s[i - len(word):i]:
                dp[i] = True
    print(dp)
    return dp[-1]

print(solution("leetcode", ["leet", "code"]))