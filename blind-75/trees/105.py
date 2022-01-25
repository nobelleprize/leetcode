# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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


def buildTree(preorder, inorder):



preorder = deserialize("[3,9,20,15,7]")
inorder = deserialize("[9,3,15,20,7]")

print(buildTree([3,9,20,15,7], [9,3,15,20,7]))
