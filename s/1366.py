# https://leetcode.com/problems/rank-teams-by-votes/

def rankTeams(votes):
    d = {}

    for vote in votes:
        for i, char in enumerate(vote):
            if char not in d:
                d[char] = [0] * len(vote)
            d[char][i] += 1
            
    voted_names = sorted(d.keys())
    return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))

print(rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
