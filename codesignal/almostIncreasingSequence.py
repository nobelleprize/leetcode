def almostIncreasingSequence(sequence):
    indx = -1
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i+1]:
            indx = i
            count += 1
        if count > 1: 
            return False
    if count==0:
        return True
    
    if count == 1:
        if indx == 0 or indx == len(sequence)-2:
            return True
        if sequence[indx-1] < sequence[indx+1] or(indx+2 < len(sequence) and sequence[indx] < sequence[indx+2]):
            return True
        
    return False
print(almostIncreasingSequence([1, 2, 1, 3, 4]))
# print(almostIncreasingSequence([1, 3, 2]))
# # print(almostIncreasingSequence([1, 2, 1, 2]))
# # print(almostIncreasingSequence([3, 6, 5, 8, 10, 20, 15]))
# print(almostIncreasingSequence([1, 1, 1, 2, 3]))
