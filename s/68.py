# https://leetcode.com/problems/text-justification/

def fullyJustify(words, maxWidth):
    n = len(words)
    i = 0 # index of current word
    ans = []
    while i < n:
        kWords = getKwords(words, maxWidth, i)
        line = insertSpace(words, maxWidth, i, kWords)
        ans.append(line)
        i += kWords
    return ans


def getKwords(words, maxWidth, i):
    kWords = 0
    line = ' '.join(words[i : i+kWords])
    while len(line) <= maxWidth and i+kWords <= len(words):
        kWords += 1
        line = ' '.join(words[i : i+kWords])
    kWords -= 1
    return kWords


def insertSpace(words, maxWidth, i, kWords):
    n = len(words)
    line = ' '.join(words[i : i+kWords])

    if kWords == 1 or i+kWords == n: # if line has only one word, or if it is last line. do left assign
        spaces = maxWidth - len(line)
        line = line + ' ' * spaces
    else:
        spaces = maxWidth - len(line) + (kWords-1)
        space = spaces // (kWords-1)
        left = spaces % (kWords-1)

        if left > 0:
            line = (' ' * (space+1)).join(words[i:i+left])
            line += ' ' * (space+1)
            line += (' ' * space).join(words[i+left : i+kWords])
        else:
            line = (' ' * space).join(words[i : i+kWords])
    return line

print(fullyJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
