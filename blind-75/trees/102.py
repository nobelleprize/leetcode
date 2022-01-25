# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    levels = []
    if not root:
        return levels
    
    helper(root, 0, levels)
    return levels
    
def helper(node, level, levels):
    if len(levels) == level:
        levels.append([])
    
    levels[level].append(node.val)

    if node.left:
        helper(node.left, level + 1, levels)
    if node.right:
        helper(node.right, level + 1, levels)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(levelOrder(root))