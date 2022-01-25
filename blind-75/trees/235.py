class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return root

root = Node(6)
root.left = Node(2)
root.left.left = Node(0)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.left.right.right = Node(5)
root.right = Node(8)
root.right.left = Node(7)
root.right.right = Node(9)

res = lowestCommonAncestor(root, root.left, root.right)
print(res.val)