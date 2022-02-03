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

print(wordsTyping(sentence = ["hello","world"], rows = 2, cols = 8)) # 1
# print(wordsTyping(sentence = ["a", "bcd", "e"], rows = 3, cols = 5)) # 2

# print(wordsTyping(sentence = ["i","had","apple","pie"], rows = 4, cols = 5)) # 1

# print(wordsTyping(["a", "bcd", "e"], 4, 6))

# def wordsTyping(sentence, rows, cols):
#     n = len(sentence)

#     # @lru_cache(None)

#     ans = 0
#     wordIdx = 0
#     for _ in range(rows):
#         ans += dp(wordIdx, cols, sentence)[1]
#         wordIdx = dp(wordIdx, cols, sentence)[0]
#     return ans

# def dp(i, cols, sentence):  # Return (nextIndex, times) if the word at ith is the beginning of the row
#     c = 0
#     times = 0
#     while c + len(sentence[i]) <= cols:
#         c += len(sentence[i]) + 1
#         i += 1
#         if i == len(sentence):
#             times += 1
#             i = 0
#     return i, times