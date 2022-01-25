# https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


def levelOrder(root):
    return helper(root, [], 0)

def helper(root, result, level):
    if root == None:
        return
        
    if len(result) == level:
        result.append([])

    result[level].append(root.val)

    helper(root.left, result, level+1)
    helper(root.right, result, level+1)

    return result

root = deserialize("[3,9,20,null,null,15,7]")
print(levelOrder(root))
