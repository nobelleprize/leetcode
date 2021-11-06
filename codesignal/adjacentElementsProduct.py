def adjacentElementsProduct(inputArray):
    highest = 0
    i = 0
    j = 1
    while j < len(inputArray):
        if inputArray[i] * inputArray[j] > highest:
            highest = inputArray[i] * inputArray[j]
        i += 1
        j += 1
    return highest

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))