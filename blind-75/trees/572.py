# https://leetcode.com/problems/subtree-of-another-tree/
from xml.sax import default_parser_list


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


def isSubtree(root, subRoot):
    if isMatch(root, subRoot): 
        return True
    if not root: 
        return False
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isMatch(root, subRoot):
    if root == None or subRoot == None:
        return root == subRoot

    return (root.val == subRoot.val and 
            isMatch(root.left, subRoot.left) and 
            isMatch(root.right, subRoot.right))


root1 = deserialize("[3,4,5,1,2]")
subRoot1 = deserialize("[4,1,2]")
print(isSubtree(root1, subRoot1)) # True

root2 = deserialize("[3,4,5,1,2,null,null,null,null,0]")
subRoot2 = deserialize("[4,1,2]")
print(isSubtree(root2, subRoot2)) # False

root3 = deserialize("[1,1]")
subRoot3 = deserialize("[1]")
print(isSubtree(root3, subRoot3)) # True

