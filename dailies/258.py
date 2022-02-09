# https://leetcode.com/problems/add-digits/

def addDigits(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
        
        if num == 0 and result > 9:
            num = result
            result = 0
    return result


print(addDigits(38))