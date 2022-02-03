import collections

secret = "acckzz"

def guess_word(word: str) -> int:
    matches = 0
    for i in range(len(word)):
        if word[i] == secret[i]:
            matches += 1
    if matches != 0:
        print("{p} matches".format(p = matches))
    else:
        print("-1")

    return matches

def findSecretWord(wordlist):
    n = 0
    count = [collections.Counter(w[i] for w in wordlist) for i in range(6)]
    while n < 6:
        # count = [collections.Counter(w[i] for w in wordlist) for i in range(6)]
        guess = max(wordlist, key=lambda w: sum(count[i][c] for i, c in enumerate(w)))
        n = guess_word(guess)
        wordlist = [w for w in wordlist if match(w, guess) == n]

def match(w1, w2):
    return sum(i == j for i, j in zip(w1, w2))

print(findSecretWord( ["ccbazz","eiowzz","abcczz", "acckzz"]))