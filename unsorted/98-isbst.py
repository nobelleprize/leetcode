# https://leetcode.com/problems/validate-binary-search-tree/

import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root) -> bool:
    return isBSTUtil(root, float("-inf"), float("inf"))

def isBSTUtil(root, minimum, maximum):
    if not root:
        return True
    
    if root.val < minimum or root.val > maximum:
        return False

    return isBSTUtil(root.left, minimum, root.val - 1) and isBSTUtil(root.right, root.val + 1, maximum)