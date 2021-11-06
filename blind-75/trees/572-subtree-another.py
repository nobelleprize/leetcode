# https://leetcode.com/problems/subtree-of-another-tree/

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def isSubtree(self, a, b):
        if not b:
            return True

        return self.dfs(a, b)
    
    def checkTree(self, a, b):
        if not a and not b:
            return True

        elif a and not b or b and not a:
            return False

        if a.val != b.val:
            return False
        
        return self.checkTree(a.left, b.left) and self.checkTree(a.right, b.right)
    
    def dfs(self, a, b):
        if not a:
            return False
            
        if a.val == b.val and self.checkTree(a, b):
            return True
        
        return self.dfs(a.left, b) or self.dfs(a.right, b)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root2 = Node(2)
root2.left = Node(4)
root2.right = Node(5)



print(root.isSubtree(root, root2))

