# https://leetcode.com/problems/delete-nodes-and-return-forest/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delNodes(root, to_delete):
    to_delete = set(to_delete)
    forest = []
    if root.val not in to_delete:
        forest.append(root)
    helper(root, to_delete, forest)

    return forest

def helper(root, to_delete, forest):
    if root is None:
        return None
    
    root.left = helper(root.left, to_delete, forest)
    root.right = helper(root.right, to_delete, forest)

    if root.val in to_delete:
        if root.left != None:
            forest.append(root.left)
        if root.right != None:
            forest.append(root.right)
        return None

    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = delNodes(root, [2, 4])
