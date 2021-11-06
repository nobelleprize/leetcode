# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if root == None:
        return []
    result = []
    queue = [root]

    while queue:
        level = []
        for _ in range(len(queue)):
            temp = queue.pop(0)
            level.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        result.append(level)
    return result



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(levelOrder(root))