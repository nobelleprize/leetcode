# https://leetcode.com/problems/find-the-town-judge/

def findJudge(n, trust):
    d = dict()
    judges = []
    for i in range(1, n+1):
        d[i] = set()
    for rel in trust:
        d[rel[0]].add(rel[1])
    for key, value in d.items():
        if value == set():
            judges.append(key)
    for judge in judges:
        del d[judge]
    

    if all(judges[0] in value for value in d.values()):
        return judges[0]
    
    # print(d)


print(findJudge(3, [[1,3],[2,3]]))
print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))