# https://leetcode.com/problems/simplify-path/

def simplifyPath(path):
    stack = []
    for portion in path.split('/'):
        if portion == "..":
            if stack:
                stack.pop()
        elif portion == '.' or not portion:
            continue
        else:
            stack.append(portion)
            
    final_str = "/" + "/".join(stack)

    return final_str

# print(simplifyPath("/home/"))
print(simplifyPath("/abc/../b/"))
# print(simplifyPath("/home//foo/"))