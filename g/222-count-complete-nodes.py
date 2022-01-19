# https://leetcode.com/problems/count-complete-tree-nodes/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root):
    if root == None:
        return 0

    d = compute_depth(root)
    left = 1
    right = 2**d - 1

    while left <= right:
        pivot = left + (right - left) // 2
        if exists(pivot, d, root):
            left = pivot + 1
        else:
            right = pivot - 1
    print(left)
    
    return (2**d - 1) + left

def compute_depth(node):
    depth = 0
    while node.left:
        node = node.left
        depth += 1
    return depth

def exists(idx, d, node):
    left = 0
    right = 2**d - 1

    for _ in range(d):
        pivot = left + (right - left) // 2
        if idx <= pivot:
            node = node.left
            right = pivot - 1 
        else:
            node = node.right
            left = pivot + 1

    return node != None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
# root.left.left.left = TreeNode(8)
# root.left.left.right = TreeNode(9)
# root.left.right.left = TreeNode(10)
# root.left.right.right = TreeNode(11)
# root.right.left.left = TreeNode(12)

print(countNodes(root))