# https://leetcode.com/problems/sentence-screen-fitting/

def wordsTyping(sentence, rows, cols):
    n = len(sentence)
    result = 0

    wordIdx = 0
    for _ in range(rows):
        c = 0  # Reset for new row

        while c + len(sentence[wordIdx]) <= cols:
            word = sentence[wordIdx]
            c += len(sentence[wordIdx]) + 1
            wordIdx += 1

            if wordIdx == n:
                result += 1
                wordIdx = 0

    return result

# print(wordsTyping(sentence = ["hello","world"], rows = 2, cols = 8)) # 1
print(wordsTyping(sentence = ["i","had","apple","pie"], rows = 4, cols = 5))