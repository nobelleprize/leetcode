class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
class Tree:
    def __init__(self):
        self.root = None
    
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data)
        inorderTraversal(root.right)

def inorderTraversal2(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data)
            curr = curr.right


def preorderTraversal(root):
    if root:
        print(root.data)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data)

def levelorderTraversal(root):
    if root is None:
        return
    
    q = []
    q.append(root)

    while len(q):
        print(q[0].data)
        node = q.pop(0)
    
        if node.left:
            q.append(node.left)
        
        if node.right:
            q.append(node.right)

def insert(root, data):
    if not root:
        root = Node(data)
        return
    
    q = []
    q.append(root)
    
    while len(q):
        root = q[0]
        q.pop(0)

        if (not root.left):
            root.left = Node(data)
            break
        else:
            q.append(root.left)

        if (not root.right):
            root.right = Node(data)
            break
        else:
            q.append(root.right)

# Given a binary tree, delete a node from it by making sure that tree shrinks from the bottom 
def deleteNode(root, key):
    key_node = None
    q = []
    q.append(root)
    temp = None

    while len(q):
        temp = q.pop(0)
        
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
    return root

def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

                
root = Node(13)
root.left = Node(12)
root.left.left = Node(4)
root.left.right = Node(19)
root.right = Node(10)
root.right.left = Node(16)
root.right.right = Node(9)

inorderTraversal(root)
deleteNode(root, 12)
print("***")
inorderTraversal(root)
