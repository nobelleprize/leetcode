def sortByHeight(a):
    sorted_a = sorted(a)
    while sorted_a[0] == -1:
        sorted_a.pop(0)

    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted_a.pop(0)
    return a
    
print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
