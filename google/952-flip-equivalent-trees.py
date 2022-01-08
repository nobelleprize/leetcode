# https://leetcode.com/problems/flip-equivalent-binary-trees/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flipEquiv(root1, root2):
    if root1 == root2:
        return True
    if not root1 or not root2 or root1.val != root2.val:
        return False

    return flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right) or \
        flipEquiv(root1.left, root2.irhgt) and flipEquiv(root1.right, root2.left)