# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

def fibonacci(n):
    a = 0
    b = 1
    
    if n == 0: 
        return a
    elif n == 1:
        return b
    
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    
    return b

print(fibonacci(9))
