class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# def inorderTraversal(root):
#     if root:
#         inorderTraversal(root.left)
#         print(root.data)
#         inorderTraversal(root.right)

def inorderTraversal(root):
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

# def preorderTraversal(root):
#     if root:
#         print(root.data)
#         preorderTraversal(root.left)
#         preorderTraversal(root.right)

def preorderTraversal(root):
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        print(curr.data)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

# def postorderTraversal(root):
#     if root:
#         postorderTraversal(root.left)
#         postorderTraversal(root.right)
#         print(root.data)

def postorderTraversal(root):
    stack1 = []
    stack2 = []
    stack1.append(root)

    while stack1:
        popped = stack1.pop()
        stack2.append(popped)
        if popped.left:
            stack1.append(popped.left)
        if popped.right:
            stack1.append(popped.right)
    while stack2:
        popped = stack2.pop()
        print(popped.data)

def levelorderTraversal(root):
    q = []
    q.append(root)
    
    while len(q):
        temp = q.pop(0)
        print(temp.data)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def height(root):
    if root is None:
        return 0
    
    else:
        l_depth = height(root.left)
        r_depth = height(root.right)

        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1   

 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postorderTraversal(root)