class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def invertTree(root):
    if root == None:
        return
    
    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)