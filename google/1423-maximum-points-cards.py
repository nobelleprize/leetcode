# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

# def maxScore(cardPoints, k):
#     frontScore = 0
#     rearScore = 0

#     for i in range(k):
#         frontScore += cardPoints[i]
    
#     result = frontScore
    
#     n = len(cardPoints)

#     for i in range(k-1, -1, -1):
#         rearScore += cardPoints[n - (k - i)]
#         frontScore -= cardPoints[i]

#         totalScore = frontScore + rearScore
#         if totalScore > result:
#             result = totalScore
#     return result


# print(maxScore([9,7,7,9,7,7,9], k = 7))

def maxScore(cardPoints, k):
    frontScore = sum(cardPoints[:k])
    rearScore = 0
    
    maxScore = frontScore
    n = len(cardPoints)

    for i in range(k-1, -1, -1):
        frontScore -= cardPoints[i]
        rearScore += cardPoints[n - (k - i)]
        if frontScore + rearScore > maxScore:
            maxScore = frontScore + rearScore
    return maxScore

print(maxScore([1,2,3,4,5,6,1], 3))
# print(maxScore([9,7,7,9,7,7,9], k = 7))
# print(maxScore([2,2,2],2))