# https://leetcode.com/problems/text-justification/

def fullJustify(words, maxWidth):
    counter = 0
    for i in range(len(words)):
        while counter + len(words[i]) <= maxWidth:
            