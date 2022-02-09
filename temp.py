def isValid(s):
    stack = []
    for paren in s:
        if paren in ['(', '[', '{']:
            stack.append(paren)
        else:
            temp = stack.pop()
            if paren == ')':
                if temp != '(':
                    return False
            elif paren == ']':
                if temp != '[':
                    return False
            else:
                if temp != '{':
                    return False
    return stack == []

print(isValid("()"))
print(isValid("(({()))"))
print(isValid("()[]{}"))