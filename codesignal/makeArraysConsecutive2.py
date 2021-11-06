def makeArrayConsecutive2(statues):
    return  max(statues) - min(statues) + 1 - len(statues)

print(makeArrayConsecutive2([6, 2, 3, 8]))