class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root) -> int:
    if root == None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    if left > right:
        return left + 1
    return right + 1


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.left.left.left = TreeNode(6)
print(maxDepth(node))