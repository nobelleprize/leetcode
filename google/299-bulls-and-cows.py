# https://leetcode.com/problems/bulls-and-cows/
from collections import defaultdict

def getHint(secret, guess):
    bulls = 0
    cows = 0
    secret_dict = defaultdict(list)
    guess_dict = defaultdict(list)
    for i in range(len(secret)):
        secret_dict[secret[i]].append(i)
        guess_dict[guess[i]].append(i)

    for key in guess_dict.keys():
        if secret_dict[key]:
            intersect = len(set(secret_dict[key]) & set(guess_dict[key]))
            bulls += intersect
            temp_cows = min(len(guess_dict[key]), len(secret_dict[key]))
            cows += temp_cows - intersect
    return "{b}A{c}B".format(b=bulls, c=cows)

# print(getHint("1807", "7810"))
# print(getHint("1123", "0111"))
print(getHint("11", "10"))