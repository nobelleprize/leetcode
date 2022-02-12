# https://leetcode.com/problems/string-to-integer-atoi/

def myAtoi(s):
    result = 0
    sign = 1
    i = 0
    n = len(s)

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    while i < n and s[i] == ' ':
        i += 1
    
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        sign = 1
        i += 1

    while i < n and s[i].isdigit():
        digit = int(s[i])

        if result > INT_MAX // 10 or \
            (result == INT_MAX // 10 and digit > INT_MAX % 10):

            if sign == 1:
                return INT_MAX
            else:
                return INT_MIN

        result = 10 * result + digit
        i += 1

    return sign * result

print(myAtoi("-0001234"))