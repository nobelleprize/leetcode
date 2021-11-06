class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isLeaf(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return 0

def sum(root):
    if root == None:
        return 0
    return sum(root.left) + root.data + sum(root.right)

def isSumTree(root):
    if root == None or isLeaf(root):
        return 1

    if isSumTree(root.left) and isSumTree(root.right):
        if root.left == None:
            left_data = 0
        elif isLeaf(root.left):
            left_data = root.left.data
        else:
            left_data = 2 * root.left.data
        
        if root.right == None:
            right_data = 0
        elif isLeaf(root.right):
            right_data = root.right.data
        else:
            right_data = 2 * root.right.data
        
        return(root.data == left_data + right_data)
    
    return 0
