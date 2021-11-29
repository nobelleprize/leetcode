# https://leetcode.com/problems/longest-string-chain/

def longestStrChain(words):
    dp = [1 for _ in range(len(words))]
    ans = 1
    words.sort(key=lambda x: len(x))

    for i in range(1, len(dp)):
        for j in range(i):
            if oneAway(words[j], words[i]) and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        ans = max(ans, dp[i])
    return max(dp)

def oneAway(w1, w2):
    if len(w1) + 1 != len(w2): 
        return False
    i = 0
    for c in w2:
        if i == len(w1): 
            return True
        if w1[i] == c:
            i += 1
    return i == len(w1)


print(oneAway("abc", "aaaa"))
# print(longestStrChain(["a","ab","ac","bd","abc","abd","abdd"]))
# print(longestStrChain(["a","b","ba","bca","bda","bdca"]))       # 4
# print(longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))  # 5
# print(longestStrChain(["abcd","dbqca"]))                      # 1
# print(longestStrChain(['a','b','c','ac','acd','aaa','bbb','awcd','abcd','awicd']))
# print(longestStrChain(["czgxmxrpx","lgh","bj","cheheex","jnzlxgh","nzlgh","ltxdoxc","bju","srxoatl","bbadhiju","cmpx","xi","ntxbzdr","cheheevx","bdju","sra","getqgxi","geqxi","hheex","ltxdc","nzlxgh","pjnzlxgh","e","bbadhju","cmxrpx","gh","pjnzlxghe","oqlt","x","sarxoatl","ee","bbadju","lxdc","geqgxi","oqltu","heex","oql","eex","bbdju","ntxubzdr","sroa","cxmxrpx","cmrpx","ltxdoc","g","cgxmxrpx","nlgh","sroat","sroatl","fcheheevx","gxi","gqxi","heheex"]))
# print(longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))