# Definition for a binary tree node.
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

def maxDepth(root):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 1

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

    # return 1 + maxDepth(root.left) + maxDepth(root.right)





root = '[3,9,20,null,null,15,7]'
print(maxDepth(deserialize(root)))
