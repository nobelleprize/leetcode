# https://leetcode.com/problems/invert-binary-tree/

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def invertTree(self, root):
        if root == None:
            return
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)



root = Node(1)
root.left = Node(2)
root.right = Node (3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(root.invertTree(root))