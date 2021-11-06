# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def maxDepth(self, root):
        if root == None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return max(leftDepth, rightDepth) + 1
        # if leftDepth > rightDepth:
            # return leftDepth + 1
        # return rightDepth + 1



root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(17)

print(root.maxDepth(root))