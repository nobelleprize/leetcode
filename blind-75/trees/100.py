class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root2 = Node(1)
root2.right = Node(2)



print(root.isSameTree(root, root2))

