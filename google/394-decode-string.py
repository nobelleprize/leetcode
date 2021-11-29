# https://leetcode.com/problems/decode-string/

def decodeString(s):
    stack = []
    for i in range(len(s)):
        if s[i] == ']':
            current = []
            num = ""
            while stack[-1] != '[':
                current.append(stack.pop())
            stack.pop()
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            num = int(num)
        
            current.reverse()
            while num > 0:
                stack.extend(current)
                num -= 1
        else:
            stack.append(s[i])

    return stack

print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")) # "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"