# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if root is None:
        return None
    
    left_res = lowestCommonAncestor(root.left, p, q)
    right_res = lowestCommonAncestor(root.right, p, q)
    
    if (left_res and right_res) or (root in [p, q]):
        return root
    else:
        return left_res or right_res

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(lowestCommonAncestor(root, root.left, root.left.right.right).val)